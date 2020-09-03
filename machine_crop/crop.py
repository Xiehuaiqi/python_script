import cv2
import os
import numpy as np

root_list = ['/home/xhq/VOC/machine/154.5cm/', '/home/xhq/VOC/machine/102cm/', '/home/xhq/VOC/machine/48cm/']
save_path = '/home/xhq/VOC/machine/all_img/'
if not os.path.exists(save_path) :
    os.mkdir(save_path)

on_list, middle_list, below_list = list(), list(), list()

nums = len(os.listdir(root_list[0]))
print(nums)
for i in root_list:
    for j in os.listdir(i):
        if i.split('/')[-2] == '154.5cm':
            on_list.append(j)
        elif i.split('/')[-2] == '102cm':
            middle_list.append(j)
        elif i.split('/')[-2] == '48cm':
            below_list.append(j)
on_list.sort()
middle_list.sort()
below_list.sort()
print(on_list, middle_list, below_list)

for i in range(nums):
    on_img = cv2.imread(root_list[0] + on_list[i])
    middle_img = cv2.imread(root_list[1] + middle_list[i])
    below_img = cv2.imread(root_list[2] + below_list[i])

    all_img = np.zeros([8703, 3024, 3], np.uint8)
    all_img[0:3272, 0:3024] = on_img[0:3272, 0:3024]
    all_img[3073:5508, 0:3024] = middle_img[761:3196, 0:3024]
    all_img[5509:8703, 0:3024] = below_img[838:4032, 0:3024]
    cv2.imwrite('{}.jpg'.format(save_path+str(i)),all_img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
    # test = cv2.resize(all_img, (640, 960))
    # cv2.imshow('all_img', test)
    # cv2.waitKey(0)
