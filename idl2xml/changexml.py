import os
import xml.etree.ElementTree as ET
xmlpath = '/home/zx/pedestrainsETH/TUD-Brussels/Annotations/'
dirpath = '/home/zx/pedestrainsETH/TUD-Brussels/ImageSets/Main/Annotations.txt'

f = open(dirpath)
lines = f.readlines()
print(len(lines))
for line in lines:
    xml = xmlpath + line.strip() + '.xml'
    print(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    for child in root:
        if child.tag == 'object':
            x1 = int(child[1][1].text)
            y1 = int(child[1][3].text)
            if x1>y1:
                child[1][1].text,child[1][3].text = child[1][3].text,child[1][1].text
            x2 = int(child[1][0].text)
            y2 = int(child[1][2].text)
            if x2>y2:
                child[1][0].text, child[1][2].text = child[1][2].text, child[1][0].text
    tree.write(xml)

# for i in lines:
#     i = i.strip('\n')
#     tree = ET.parse(xmlpath + i +'.xml')
#     root = tree.getroot()
#
#     root[0].text = 'JPEGImages'
#     root[1].text = i +'jpg'
#     root[2].text = imgpath + i + 'jpg'
#     print(root[0].text)
#     print(root[1].text)
#     print(root[2].text)
#     tree.write(xmlpath + i +'.xml')