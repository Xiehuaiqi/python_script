# -*- coding:utf-8 -*-
import os, glob
import cv2
from scipy.io import loadmat
from collections import defaultdict
import numpy as np
from lxml import etree, objectify

def visualize_bbox(xml_file, img_file):

    tree = etree.parse(xml_file)
    # load image
    image = cv2.imread(img_file)
    origin = cv2.imread(img_file)
    for obj in tree.xpath('//object'):
        word_class = obj[0].text
        bbox = obj[1]
        # 获取一张图片的所有bbox
        # for bbox in tree.xpath('//bndbox'):
        coord = []
        for corner in bbox.getchildren():
            coord.append(int(float(corner.text)))
        print (coord)
        cv2.rectangle(image, (coord[0], coord[1]), (coord[2], coord[3]), (0, 0, 255), 2)
        cv2.putText(image, word_class, (coord[0], coord[1]), cv2.FONT_HERSHEY_SIMPLEX , 0.6, (0, 255, 0), 2)
        # visualize image
    cv2.imshow("test", image)
    cv2.imshow('origin', origin)
    # cv2.imwrite('/home/zx/博士VOC/MOT17VOC/detect/MOT17-09_' + str(i) + '.jpg', image)
    # cv2.imwrite('/home/zx/博士VOC/MOT17VOC/detect',image)
    cv2.waitKey(0)

xml_file = "/home/zx/VOC2042/Annotations/hiv01_201902261800_201902261854_000001088.xml"
img_file = "/home/zx/VOC2042/JPEGImages/hiv01_201902261800_201902261854_000001088.jpg"
visualize_bbox(xml_file, img_file)
# for i in range(1,601):
#     xml_file = "/home/zx/博士VOC/MOT17VOC/Annotations/MOT17-09_"+ str(i) +".xml"
#     img_file = "/home/zx/博士VOC/MOT17VOC/JPEGImages/MOT17-09_"+ str(i) +".jpg"
#     visualize_bbox(xml_file, img_file)