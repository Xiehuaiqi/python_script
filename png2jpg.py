# -*-coding:utf-8-*-
import cv2

import os
path = '/home/xiehuaiqi/Pictures/coal_estimate/1/'

for name in os.listdir(path):
    if name[-3:]=='png':
        print(name[-3:])
        img = cv2.imread(path+name)
        jpg_name = name[:-3]+'jpg'
        cv2.imwrite(path+jpg_name,img)