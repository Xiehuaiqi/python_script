#coding:utf-8
import cv2
import os
import makedir1 as mk1
import makemenudir as mkm


menudir = mkm.main()
# print dirname
for j in menudir:
    # print j
    #folds = os.listdir('/home/zx/UCF-101/'+ j)
    folds = mk1.main('/home/zx/UCF-101/'+ j)
    for i in folds:
        video_path = '/home/zx/UCF-101/'+ j + '/' + i + '.avi'
        dir_name_path = '/home/zx/UCF-101/'+ j + '/' + i +'/'
        print video_path
        print dir_name_path
        vc = cv2.VideoCapture(video_path)  # 读入视频文件
        c = 1

        if vc.isOpened():  # 判断是否正常打开
            rval, frame = vc.read()
        else:
            rval = False

        timeF = 1  # 视频帧计数间隔频率
        os.mkdir('/home/zx/UCF-101/' + j + '/' + i)
        while rval:  # 循环读取视频帧
            rval, frame = vc.read()
            if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                cv2.imwrite(dir_name_path  + str(c) + '.jpg', frame)  # 存储为图像
            c = c + 1
            cv2.waitKey(1)
        vc.release()
        os.system("rm " + '/home/zx/UCF-101/'+ j + '/' + i + '.avi')