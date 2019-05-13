#-*-coding:utf-8 -*-

import os
import sys
import makedir1 as mk1
import makedir2 as mk2

def compare(file1,file2):
    f1=open(file1)
    f2=open(file2)
    lines1=f1.readlines()
    lines2=f2.readlines()
    print(len(lines1))
    print(len(lines2))
    #output = sys.stdout
    #outputfile = open('/home/zx/labelImg/bus_case/more1.txt','w')
    #sys.stdout = outputfile
    for line1 in lines1:
         # if line1 not in lines2:
         #     print(line1)
        txtlist = []
        if line1 in lines2:
            txtlist.append[line1]
    mk1.text_save(txtlist,'/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/same.txt')
    #outputfile.close()
    #sys.stdout = output
if __name__ == '__main__':
    mk1.main()
    mk2.main()
    compare('/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/Annotations.txt','/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/JEPT.txt')
