#coding:utf-8
import cv2
import os
import makedir1 as mk1
from time import sleep
from tqdm import tqdm

path = '/home/zx/desktop/atm监控/视频数据/锡山_环/'
dirname = mk1.main(path)
print dirname
for i in dirname:
    video_path = path + i + '.mp4'  #改后缀格式
    dir_name_path = path + i +'/'
    print video_path
    #print dir_name_path
    vc = cv2.VideoCapture(video_path)  # 读入视频文件
    c = 1
    frames_num = vc.get(7)
    print frames_num
    break
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
    else:
        rval = False

    timeF = 300  # 视频帧计数间隔频率30每秒一帧，1每秒30帧
    os.mkdir(path + i)

    for i in tqmd(range(int(frames_num))):
        sleep(0.5)
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()

        if (c % timeF == 0):  # 每隔timeF帧进行存储操作
            cv2.imwrite(dir_name_path  + str(c) + '.jpg', frame)  # 存储为图像
        c = c + 1
        cv2.waitKey(1)

    vc.release()

    # cv2.namedWindow("1",cv2.WINDOW_FREERATIO)
    # cv2.imshow("11",rgb_image)
    # cv2.waitKey(10)
