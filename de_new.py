import numpy as np  
import sys,os  
import cv2
import xml.etree.ElementTree as ET
import pdb
from caffe.proto import caffe_pb2
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
caffe_root = '/opt/mobilessd/caffe/'
sys.path.insert(0, caffe_root + 'python')  
import caffe
  
save_dir = '/opt/mobilessd/caffe/examples/MobileNet-SSD/xml/'

net_file= 'no_bn.prototxt'  
caffe_model='no_bn.caffemodel'  
#test_dir = "testSet"

small_img_w_length = 1000
small_img_h_length = 1000
img_height_overlap = 30
img_width_overlap = 30
image_path = "testSet"
small_img_path = "small_image"
small_image_result = "small_image_result"

if not os.path.exists(caffe_model):
    print(caffe_model + " does not exist")
    exit()
if not os.path.exists(net_file):
    print(net_file + " does not exist")
    exit()
    
net = caffe.Net(net_file,caffe_model,caffe.TEST)

def preprocess(src):
    img = cv2.resize(src, (300,300))
    img = img - 127.5
    img = img * 0.007843
    return img

def my_nms(dets, thresh):
    
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    
    order = scores.argsort()[::-1]
    

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

       
      
        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]

    return keep

def save_result(image_file, dets, thresh=0.015):

    img = cv2.imread(os.path.join(image_path,image_file))
    height, width, channels = img.shape
    print(width, height)
    inds = np.where(dets[:, -1] >= thresh)[0]
    if len(inds) == 0:
        return

    #nms
    nms_ret = my_nms(dets, 0.25)
    dets = dets[nms_ret, :]
    inds = np.where(dets[:, -1] >= thresh)[0]

    #output bbox xml message
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
   
    for i in inds:
        bbox = dets[i, :4]
        score = dets[i, -1]

        #left, top, right, bottom = trainFile[1], trainFile[2], trainFile[3] , trainFile[4]
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
        confidence = round(score,1)
        # cv2.putText(img, item[-1] + ":" + str(confidence), (xmin, ymax), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(200,255,155),thickness=2)
        cv2.putText(img, str(confidence), (bbox[0], bbox[3]), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(200,255,155),thickness=2)

    xml = tostring(node_root, pretty_print=True)    
    dom = parseString(xml)
    if image_file.split(".")[1] == 'png':
        save_ml = os.path.join(save_dir, image_file.replace('png', 'xml'))
    else:
        save_ml = os.path.join(save_dir, image_file.replace('jpg', 'xml'))
    with open(save_ml, 'wb') as f:
        f.write(xml)

    cv2.imwrite("testResult/{}".format(str(image_file)), img) 


def detect(imgfile):
    origimg = cv2.imread(os.path.join(small_img_path, imgfile))
    img = preprocess(origimg)
    img = img.astype(np.float32)
    img = img.transpose((2, 0, 1))

    net.blobs['data'].data[...] = img
    out = net.forward() 
    
    conf_thresh = 0.15
    topn = 50 
    h = img.shape[0]
    w = img.shape[1]

    det_label = out['detection_out'][0,0,:,1]
    det_conf = out['detection_out'][0,0,:,2]
    det_xmin = out['detection_out'][0,0,:,3]
    det_ymin = out['detection_out'][0,0,:,4]
    det_xmax = out['detection_out'][0,0,:,5]
    det_ymax = out['detection_out'][0,0,:,6]


    top_indices = [i for i, conf in enumerate(det_conf) if conf >= conf_thresh]
    top_conf = det_conf[top_indices]
    top_label_indices = det_label[top_indices].tolist()
    #top_labels = get_labelname(labelmap, top_label_indices)
    top_xmin = det_xmin[top_indices]
    top_ymin = det_ymin[top_indices]
    top_xmax = det_xmax[top_indices]
    top_ymax = det_ymax[top_indices]

    result = []
    #for i in range(len(box)):
    for i in range(min(topn, top_conf.shape[0])):
        xmin = top_xmin[i] 
        ymin = top_ymin[i] 
        xmax = top_xmax[i] 
        ymax = top_ymax[i] 
        score = top_conf[i]
        label = int(top_label_indices[i])
        #label_name = top_labels[i]
        #result.append([xmin, ymin, xmax, ymax, label, score, label_name])
        result.append([xmin, ymin, xmax, ymax, label, score])
    return result

if __name__=='__main__':
    im_names = []
    
    for filename in os.listdir(os.path.join(image_path, '')):
        if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png"):
            im_names.append(filename)
    print(im_names)

    for image_file in im_names:
        # Split to small images
        
        split_info = split_image(image_file)
        
        results = np.empty([1, 5], dtype=np.float32)
        print (results.shape )
        #split_info:(x_start, x_end, y_start, y_end, left, top, img_file_name)
        for small_image in split_info:
            result = detect(small_image[6])
            
            sWidth = small_image[1] - small_image[0]
            sHeight = small_image[3] - small_image[2]

            print("image_file:",small_image[6])
            bbox_num = 0

            print ("sWidth,sHeight:",sWidth,sHeight)
            s = max(sWidth,sHeight)
            print ("s:",s)         
            #result:[xmin, ymin, xmax, ymax, label, score]

        nms_ret = my_nms(results, 10)
        # print(nms_ret)
        final_results = results[nms_ret, :]
        save_result(image_file, final_results)

