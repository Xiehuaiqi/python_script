import os
path = '/home/zx/desktop/baidu-label/'
for i in range(0,501):
    print(i)
    t = str(input())
    os.system("mv " + path +  str(i) +".png " + path + t +".png")