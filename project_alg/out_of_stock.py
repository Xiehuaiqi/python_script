import numpy as np
import sys, os
import cv2
import caffe


class out_of_stock(object):
    def __init__(self):
        net_file = 'MobileNetSSD_deploy.prototxt'
        caffe_model = 'mobilenet_iter_66000.caffemodel'
        self.net = caffe.Net(net_file, caffe_model, caffe.TEST)
        CLASSES = ('background', 'mono_oos')

    def preprocess(self,src):
        img = cv2.resize(src, (300, 300))
        img = img - 127.5
        img = img * 0.007843
        return img

    def postprocess(self,img, out):
        h = img.shape[0]
        w = img.shape[1]
        box = out['detection_out'][0, 0, :, 3:7] * np.array([w, h, w, h])
        cls = out['detection_out'][0, 0, :, 1]
        conf = out['detection_out'][0, 0, :, 2]
        return (box.astype(np.int32), conf, cls)

    def detect(self,imgfile):
        origimg = cv2.imread(imgfile)
        img = self.preprocess(origimg)

        img = img.astype(np.float32)
        img = img.transpose((2, 0, 1))

        self.net.blobs['data'].data[...] = img
        out = self.net.forward()
        box, conf, cls = self.postprocess(origimg, out)
        print(box,conf,cls)
        n = len(conf)
        print(n)
        local_empty = []
        for i in range(len(box)):
            p1 = (box[i][0], box[i][1])
            p2 = (box[i][2], box[i][3])
            cv2.rectangle(origimg, p1, p2, (0, 255, 0), 2)
            p3 = (max(p1[0], 15), max(p1[1], 15))
            local_empty.append({box[i][0],box[i][1],box[i][2],box[i][3],conf[i],cls[i]})
        return local_empty

    def detect(self,imgfile):
        origimg = cv2.imread(imgfile)
        img = self.preprocess(origimg)

        img = img.astype(np.float32)
        img = img.transpose((2, 0, 1))

        self.net.blobs['data'].data[...] = img
        out = self.net.forward()
        box, conf, cls = self.postprocess(origimg, out)
        print(box,conf,cls)
        n = len(conf)
        print(n)
        local_empty = []
        for i in range(len(box)):
            p1 = (box[i][0], box[i][1])
            p2 = (box[i][2], box[i][3])
            cv2.rectangle(origimg, p1, p2, (0, 255, 0), 2)
            p3 = (max(p1[0], 15), max(p1[1], 15))
            local_empty.append({box[i][0],box[i][1],box[i][2],box[i][3],conf[i],cls[i]})
        return local_empty


if __name__ == '__main__':
    t = out_of_stock()
    print(t.detect('/opt/mobilessd/examples/MobileNet-SSD/images/48cmWechatIMG108.jpeg'))
