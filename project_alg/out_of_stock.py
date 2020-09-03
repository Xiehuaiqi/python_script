# -*- coding:utf-8 -*-
import numpy as np
import sys, os
import cv2
import caffe


class out_of_stock(object):
    def __init__(self):
        net_file = 'MobileNetSSD_deploy.prototxt'
        caffe_model = 'mobilenet_iter_66000.caffemodel'
        self.net = caffe.Net(net_file, caffe_model, caffe.TEST)
        self.CLASSES = ('background', 'mono_oos')

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

    def detect_all(self, img_up, img_mid, img_down, mid_overlap=0, down_overlap=0, mid_offset=0, down_offset=0):

        whole_img = cv2.imread()
        img_all = [img_up, img_mid, img_down]
        result_all = []
        #loc为上中下相机位置，origimg为相机参数
        for loc, origimg in enumerate(img_all):
            img = self.preprocess(origimg)

            img = img.astype(np.float32)
            img = img.transpose((2, 0, 1))

            self.net.blobs['data'].data[...] = img
            out = self.net.forward()
            box, conf, cls = self.postprocess(origimg, out)
            n = len(conf)
            local_empty = []
            for i in range(n):
                p1 = (box[i][0], box[i][1])
                p2 = (box[i][2], box[i][3])
                if loc == 1:
                    box[i][0] +=
                cv2.rectangle(origimg, p1, p2, (0, 255, 0), 2)
                local_empty.append({box[i][0], box[i][1], box[i][2], box[i][3], conf[i], cls[i]})
                # 可视化
                p3 = (max(p1[0], 15), max(p1[1], 15))
                title = "%s:%.2f" % (self.CLASSES[int(cls[i])], conf[i])
                cv2.putText(origimg, title, p3, cv2.FONT_ITALIC, 1, (0, 255, 0), 2)
            cv2.imwrite('{}.jpg'.format(loc), origimg)
            result_all.append(local_empty)
        # print(result_all)
        return result_all


if __name__ == '__main__':
    t = out_of_stock()

    up_img = cv2.imread()
    mid_img = cv2.imread()
    down_img = cv2.imread()
    print(t.detect_all(up_img, mid_img, down_img))
