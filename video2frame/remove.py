#coding:utf-8
import os
from PIL import Image
seq = 1
path = "/media/zx/TOSHIBA EXT/预留孔洞-临边防护/合规/"
for filename in os.listdir(r"/media/zx/TOSHIBA EXT/预留孔洞-临边防护/合规"):
    if seq>=1:
        #os.system("nautilus " + path + filename)

        print(seq)
        print(filename)
        for j in os.listdir(r"/media/zx/TOSHIBA EXT/预留孔洞-临边防护/合规/"+filename):
            #os.system('explorer.exe /n,/home/zx/desktop/Yawning'+filename)
            #print(j)
            #img = Image.open(j)
            os.system("eog "+path+filename+"/1.jpg" )
            de = input("input 1 delete:")
            if de==1:
                p = input("start: ")
                #p +=10000
                t = input("end:   ")
                #t +=10000
                print(t)
                for i in range(p,t+1):
                    os.system("rm " + path + filename+'/' +str(i) + ".jpg")
                q = input("input 1 delete\nnext input 0:")
                if q==0:
                    break
                else:
                    pass
            else:
                #close dir
                break
    seq += 1
