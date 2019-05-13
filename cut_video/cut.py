# -*- coding: UTF-8 -*-
from cv2 import VideoCapture,imwrite,waitKey
from os import system
from sys import argv
from PIL import Image


#传入命令行参数
video_path = argv[1]
argu = int(argv[2])

vc = VideoCapture(video_path)

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False

if rval:
    rval, frame = vc.read()
    imwrite("example.jpg", frame)
    img = Image.open("example.jpg")
    width = img.size[0]
    height = img.size[1]
    waitKey(1)
    vc.release()
    system('rm example.jpg')
    # ffmpeg 切分视频
    if argu == 2:
        system('ffmpeg -i '+ video_path +' -strict -2 -vf crop='+ str(width) +':'+ str(height/2) +':0:0 '+video_path.split('.')[0]+'_new2.mp4')
    elif argu == 3:
        system('ffmpeg -i '+ video_path +' -strict -2 -vf crop='+ str(width) +':'+ str(height/3) +':0:0 '+video_path.split('.')[0]+'_new3.mp4')
    elif argu == 4:
        system('ffmpeg -i '+ video_path +' -strict -2 -vf crop='+ str(width) +':'+ str(height/4) +':0:0 '+video_path.split('.')[0]+'_new4.mp4')
else:
    print('NO FILE FOUNED')