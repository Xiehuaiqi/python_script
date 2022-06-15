# -*-coding:utf-8-*-
import os

path = '/home/xiehuaiqi/PycharmProjects/VOC/coal_estimation/JPEGImages/'
save_path = '/home/xiehuaiqi/PycharmProjects/VOC/coal_estimation/ImageSets/Segmentation/trainval.txt'
filename = []
for dir in os.listdir(path):
    name = dir.split('.')[0]+'\n'
    filename.append(name)
with open(save_path,'w') as f:
    for i in filename:
        f.write(i)
f.close();
    
    
