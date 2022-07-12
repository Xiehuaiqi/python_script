# -*-coding:utf-8-*-
import cv2
import numpy
import shutil
import os
#全黑的灰度图
gray0=numpy.zeros((1080,1920),dtype=numpy.uint8)
# Img_rgb=cv2.cvtColor(gray0,cv2.COLOR_GRAY2RGB)
#将RGB通道全部置成0
# Img_rgb[:,:,:]=0
cv2.imwrite('test.png',gray0)
# cv2.imshow('0',gray0)
# cv2.waitKey(0)


image = "test.png"
path = '/home/xiehuaiqi/Pictures/煤量估计空_mask/'
if os.path.exists(path):
    new_path = os.getcwd() + '/'+image
    print(new_path)

    for i in range(70):
        shutil.copyfile(new_path,path+str(i)+'_null.png')