import numpy as np
import sys,os
import cv2
import xml.etree.ElementTree as ET
from caffe.proto import caffe_pb2
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import caffe

net_file = 'example/MobileNetSSD_deploy.prototxt'
caffe_model = 'snapshot/mobilenet_iter_66000.caffemodel'
test_dir = "images"
save_dir = 'xml/'

if not os.path.exists(caffe_model):
    print(caffe_model + " does not exist")
    exit()
if not os.path.exists(net_file):
    print(net_file + " does not exist")
    exit()
caffe.set_device(2)
net = caffe.Net(net_file, caffe_model, caffe.TEST)

CLASSES = ('background',
           'mono_oos')


def preprocess(src):
    img = cv2.resize(src, (300, 300))
    img = img - 127.5
    img = img * 0.007843
    return img


def postprocess(img, out):
    h = img.shape[0]
    w = img.shape[1]
    box = out['detection_out'][0, 0, :, 3:7] * np.array([w, h, w, h])

    cls = out['detection_out'][0, 0, :, 1]
    conf = out['detection_out'][0, 0, :, 2]
    return (box.astype(np.int32), conf, cls)


def detect(imgfile):mport numpy as np
import sys,os
import cv2
import xml.etree.ElementTree as ET
from caffe.proto import caffe_pb2
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
    origimg = cv2.imread(imgfile)
    img = preprocess(origimg)

    img = img.astype(np.float32)
    img = img.transpose((2, 0, 1))

    net.blobs['data'].data[...] = img
    out = net.forward()
    box, conf, cls = postprocess(origimg, out)

    for i in range(len(box)):
        p1 = (box[i][0], box[i][1])
        p2 = (box[i][2], box[i][3])
        cv2.rectangle(origimg, p1, p2, (0, 255, 0), 2)
        p3 = (max(p1[0], 15), max(p1[1], 15))

        title = "%s:%.2f" % (CLASSES[int(cls[i])], conf[i])
        cv2.putText(origimg, title, p3, cv2.FONT_ITALIC, 1, (0, 255, 0), 2)
    # cv2.imshow("SSD", origimg)
    cv2.imwrite('./result/{}.jpg'.format(imgfile.split('/')[-1]), origimg)
    save_result(imgfile, box, conf)
    # k = cv2.waitKey(0) & 0xff
    # Exit if ESC pressed
    # if k == 27 : return False
    # return True


def save_result(image_file, box, conf):
    img = cv2.imread(os.path.join(test_dir + "/" + f))
    height, width, channels = img.shape
    # output bbox xml message
    node_root = Element('annotation')

    node_folder = SubElement(node_root, 'folder')
    node_folder.text = 'IMAGE'

    node_filename = SubElement(node_root, 'filename')
    node_filename.text = image_file

    node_size = SubElement(node_root, 'size')
    node_width = SubElement(node_size, 'width')
    node_width.text = '%s' % width
    node_height = SubElement(node_size, 'height')
    node_height.text = '%s' % height

    node_depth = SubElement(node_size, 'depth')
    node_depth.text = '%s' % 3

    for i in len(box):
        bbox = box
        score = conf

        # left, top, right, bottom = trainFile[1], trainFile[2], trainFile[3] , trainFile[4]
        node_object = SubElement(node_root, 'object')
        node_name = SubElement(node_object, 'name')
        node_name.text = 'object'
        node_difficult = SubElement(node_object, 'difficult')
        node_difficult.text = '0'
        node_bndbox = SubElement(node_object, 'bndbox')
        node_xmin = SubElement(node_bndbox, 'xmin')
        node_xmin.text = '%s' % bbox[0]
        node_ymin = SubElement(node_bndbox, 'ymin')
        node_ymin.text = '%s' % bbox[1]
        node_xmax = SubElement(node_bndbox, 'xmax')
        node_xmax.text = '%s' % bbox[2]
        node_ymax = SubElement(node_bndbox, 'ymax')
        node_ymax.text = '%s' % bbox[3]

        cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 5)
        confidence = round(score, 1)
        # cv2.putText(img, item[-1] + ":" + str(confidence), (xmin, ymax), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(200,255,155),thickness=2)
        cv2.putText(img, str(confidence), (bbox[0], bbox[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(200, 255, 155),
                    thickness=2)

    xml = tostring(node_root, pretty_print=True)
    dom = parseString(xml)
    if image_file.split(".")[1] == 'png':
        save_ml = os.path.join(save_dir, image_file.replace('png', 'xml'))
    else:
        save_ml = os.path.join(save_dir, image_file.replace('jpg', 'xml'))
    with open(save_ml, 'wb') as f:
        f.write(xml)


for f in os.listdir(test_dir):
    print(test_dir + "/" + f)
    if detect(test_dir + "/" + f) == False:
        break
