# -*-coding:utf-8-*-
import os

path = '/home/xiehuaiqi/Pictures/vlc_截图/'

for num,name in enumerate(os.listdir(path)):
    print(name,num)
    # os.system('mv '+path+name+' {}{}.jpg'.format(path,str(num)))