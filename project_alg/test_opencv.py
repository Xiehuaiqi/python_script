import cv2
import os
path = '/home/xhq/VOC/machine/small_voc/images/'
save_path = '/home/xhq/VOC/machine/small_voc/new_img/'
for i in os.listdir(path):
    img = cv2.imread(path+i)
    cv2.imwrite(save_path+i.split('.')[0]+'.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
    # cv2.imshow('img',img)
    # cv2.waitKey(0)