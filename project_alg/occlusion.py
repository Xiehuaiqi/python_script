import numpy as np
import sys, os
import cv2
import caffe


class occlusion(object):
    def __init__(self):
        net_file = 'MobileNetSSD_deploy.prototxt'
        caffe_model = 'mobilenet_iter_30000.caffemodel'
        self.net = caffe.Net(net_file, caffe_model, caffe.TEST)

    def preprocess(self, src):
        img = cv2.resize(src, (300, 300))
        img = img - 127.5
        img = img * 0.007843
        return img

    def postprocess(self, img, out):
        h = img.shape[0]
        w = img.shape[1]
        box = out['detection_out'][0, 0, :, 3:7] * np.array([w, h, w, h])
        cls = out['detection_out'][0, 0, :, 1]
        conf = out['detection_out'][0, 0, :, 2]
        return (box.astype(np.int32), conf, cls)

    def detect(self, imgfile):
        origimg = cv2.imread(imgfile)
        img = self.preprocess(origimg)
        img = img.astype(np.float32)
        img = img.transpose((2, 0, 1))

        self.net.blobs['data'].data[...] = img
        out = self.net.forward()

        box, conf, cls = self.postprocess(origimg, out)
        occlusion = 0  # 遮挡参数,遮挡是1,未遮挡为0
        for i in range(len(box)):
            if conf[i] > 0.6:
                occlusion = 1
                break
        return occlusion


if __name__ == '__main__':
    t = occlusion()
    print(t.detect('/opt/occlusion/image/18-5_2.jpg'))
