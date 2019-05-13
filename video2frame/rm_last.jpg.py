#coding:utf-8
import os

file_path = '/home/zx/desktop/atm监控/视频数据/DVR_锡山ATM环境2070000-100000/'

os.system("find "+file_path+" -name "+"'*' -type f -size 0c | xargs -n 1 rm -f")
