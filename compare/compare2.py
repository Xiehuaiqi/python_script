#-*-coding:utf-8 -*-

import os
import sys
import makedir1 as mk1
import makedir2 as mk2
def compare(file1,file2):
    f1=open(file1)
    f2=open(file2)
    xml=f1.readlines()
    jepg=f2.readlines()
    print(len(xml))
    print(len(jepg))
    #output = sys.stdout
    #outputfile = open('/home/zx/labelImg/bus_case/more1.txt','w')
    #sys.stdout = outputfile

    for line1 in jepg:
        if line1 not in xml:
            print(line1)
    #outputfile.close()
    #sys.stdout = output
if __name__ == '__main__':
    mk1.main()
    mk2.main()
    compare('/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/Annotations.txt','/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/JEPT.txt')
