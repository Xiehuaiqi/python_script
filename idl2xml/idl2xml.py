#coding:utf-8
import re
import os
import sys
import xml.etree.ElementTree as ET
from beautiful import prettyXml
source_path = "/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/yimg-000-0.xml"
goal_path = "/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-MotionPairs/additional-negative-bootstrap/Annotations/"

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


ano = open("/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-MotionPairs/additional-negative-bootstrap/annotation.idl")
lines = ano.readlines()
num = 0
for line in lines:
    if ":" in line:
        num += 1
        #以冒号为标记分割
        line = line.split(":")
        print line[0],line[1]

        name = eval(line[0]).split(".")
        # 取出标记坐标
        print name[0]
        mark = re.sub("\D", " ", line[1])
        mark = mark.strip()
        #分割为列表
        mark = mark.split()
        print type(mark)
        print mark
        length = len(mark)
        print length
        os.system("scp " + source_path + " "+goal_path)
        os.system("mv " + goal_path +"/yimg-000-0.xml "+ \
                  goal_path+name[0]+".xml" )
        #解析lixml文件
        tree = ET.parse(goal_path+name[0]+".xml")
        root = tree.getroot()
        root[1].text = name[0]+".jpg"
        #保存xml树结构
        if length / 4 == 1:
            root[5][1][0].text = mark[0]
            root[5][1][1].text = mark[1]
            root[5][1][2].text = mark[2]
            root[5][1][3].text = mark[3]
        else:
            root[5][1][0].text = mark[0]
            root[5][1][1].text = mark[1]
            root[5][1][2].text = mark[2]
            root[5][1][3].text = mark[3]
            for i in range(1,length/4):
                element = ET.Element('object')
                one = ET.Element('name')
                one.text = 'person'
                element.append(one)
                two = ET.Element('bndbox')
                two1 = ET.Element('xmin')
                two1.text = mark[i*4]
                two.append(two1)
                two2 = ET.Element('ymin')
                two2.text = mark[i*4+1]
                two.append(two2)
                two3 = ET.Element('xmax')
                two3.text = mark[i*4+2]
                two.append(two3)
                two4 =ET.Element('ymax')
                two4.text = mark[i*4+3]
                two.append(two4)
                element.append(two)
                three = ET.Element('difficult')
                three.text = '0'
                element.append(three)
                four = ET.Element('occlusion')
                four.text='0'
                element.append(four)
                root.append(element)
                prettyXml(root, '  ', '\n')
                # tree.write(goal_path + name[0] + ".xml")
                # sys.exit()
        tree.write(goal_path+name[0]+".xml")

print(num)
print(len(lines))