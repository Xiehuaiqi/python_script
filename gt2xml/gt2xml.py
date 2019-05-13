#coding:utf-8
import re
import os
import sys
import xml.etree.ElementTree as ET
import glob
from beautiful import prettyXml

source_path = "/home/zx/博士VOC/MOT17VOC/img-001-2.xml"
goal_path = "/home/zx/博士VOC/MOT17VOC/Annotations/"
label = ['Pedestrian','Person on vehicle','Car','Bicycle','Motorbike','Non motorized vehicle','Static person','Distractor','Occluder','Occluder on the ground','Occluder full','Reflection']

def save_xml(self, file_name):
    xml_str = self.m_dom.toprettyxml(indent="    ")
    repl = lambda x: ">%s</" % x.group(1).strip() if len(x.group(1).strip()) != 0 else x.group(0)
    pretty_str = re.sub(r'>\n\s*([^<]+)</', repl, xml_str)
    open(file_name, 'w').write(pretty_str)

def get_files(file_dir):

    namelist = []
    for file in os.listdir(file_dir):
        name = file.split('.')
        namelist.append(name[0])
    return(namelist)

def parseXML():
    # 保存xml树结构
    element = ET.Element('object')
    one = ET.Element('name')
    one.text = label[cls_num-1]
    element.append(one)
    two = ET.Element('bndbox')
    two1 = ET.Element('xmin')
    two1.text = xmin
    two.append(two1)
    two2 = ET.Element('ymin')
    two2.text = ymin
    two.append(two2)
    two3 = ET.Element('xmax')
    two3.text = xmax
    two.append(two3)
    two4 = ET.Element('ymax')
    two4.text = ymax
    two.append(two4)
    element.append(two)
    three = ET.Element('difficult')
    three.text = '0'
    element.append(three)
    four = ET.Element('occlusion')
    four.text = '0'
    element.append(four)
    root.append(element)

num = 0

images_path = '/home/zx/博士VOC/MOT17VOC/MOT17-05/*.txt'

for image_file in glob.glob(images_path):
    print(image_file)
    ano = open(image_file)
    lines = ano.readlines()
    ano_num = len(lines)  #标注的数量
    image_split_name = image_file.split('/')[-1].split('.')[0]
    print(image_split_name)
    os.system("scp " + source_path + " " + goal_path)
    os.system("mv " + goal_path + "/img-001-2.xml " + \
              goal_path + image_split_name + ".xml")
    # 解析lixml文件
    tree = ET.parse(goal_path + image_split_name + ".xml")
    root = tree.getroot()
    root[1].text = image_split_name + ".jpg"

    for line in lines:
        num += 1
        #以冒号为标记分割
        line = line.split(",")
        cls = line[0]
        xmin = line[2]
        ymin = line[3]
        xmax = str(int(line[2])+int(line[4]))
        ymax = str(int(line[3])+int(line[5]))
        cls_num = int(line[-2])
        parseXML()
        prettyXml(root, '  ', '\n')
        # tree.write(goal_path + name[0] + ".xml")
        # sys.exit()
    tree.write(goal_path+ image_split_name +".xml")

print num
print len(lines)