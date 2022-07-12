# -*-coding:utf-8-*-
import os,cv2

path = '/home/xiehuaiqi/Pictures/vlc_截图/'
for i in os.listdir(path):
    img = cv2.imread(path+i)
    print(img.shape)
    # cv2.imshow('test',img)
    # cv2.waitKey(0)
