import os
import glob

import cv2
import matplotlib.pyplot as plt
#
images_path = '/home/zx/博士VOC/train/'
num = 0
list = os.listdir(images_path) #改
dir = 'img1'
namelist = []
def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

for i in list:
    path = os.path.join(images_path,i)
    path_c = os.path.join(path,dir)
    for image_file in os.listdir(path_c):#改path
        # plt.imshow(image_file)
        image_file = os.path.join(path_c,image_file)
        # print(image_file)
        num += 1
        name = image_file.split('/')
        name_last = int(str(name[-1].split('.')[0]))
        name_new = name[-3]+'_'+ str(name_last)

        name_txt = name_new.split('.')[0]
        namelist.append(name_txt)
        # print(name)

        os.system('mv '+ image_file +' /home/zx/博士VOC/train/'+name[-3]+'/'+name[-2]+'/' +name_new)
        os.system('mv '+'/home/zx/博士VOC/train/'+name[-3]+'/'+name[-2]+'/' +name_new +' /home/zx/博士VOC/train/')
    #  break
    # break
print(num)
text_save(namelist, '/home/zx/博士VOC/MOT17VOC/Annotations/Annotations.txt')