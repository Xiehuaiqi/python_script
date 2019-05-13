import os
import xml.etree.ElementTree as ET
xmlpath = '/home/zx/SCUT_HEAD_Part_B/Annotations/'
imgpath = '/home/zx/SCUT_HEAD_Part_B/JPEGImages/'

f = open('1.txt')
lines = f.readlines()
print(len(lines))

for i in lines:
    i = i.strip('\n')
    tree = ET.parse(xmlpath + i +'.xml')
    root = tree.getroot()

    root[0].text = 'JPEGImages'
    root[1].text = i +'jpg'
    root[2].text = imgpath + i + 'jpg'
    print(root[0].text)
    print(root[1].text)
    print(root[2].text)
    tree.write(xmlpath + i +'.xml')