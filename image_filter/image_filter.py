import os
import shutil
path_image_source = '/home/xiehuaiqi/Pictures/行车行人/'
path_image_des = '/home/xiehuaiqi/Pictures/行车/'
path_txt = '/home/xiehuaiqi/PycharmProjects/yolov5-5.0/runs/detect/exp45/labels/'

for i in os.listdir(path_txt):
    with open(path_txt+i,'r') as file_label:
        res = file_label.readlines()
        for j in res:
            if int(j[0]) == 0:
                img = i.split('.')[0] +'.jpg'
                shutil.copy(os.path.join(path_image_source,img),path_image_des)
            # print(j[0])
            # exit()
