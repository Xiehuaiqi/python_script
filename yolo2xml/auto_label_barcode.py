import os, cv2, shutil, sys
import argparse
from xml.dom import minidom
import torch.backends.cudnn as cudnn
import yaml
import numpy as np

img_size = 800

def cut_img():
    for img_name in os.listdir(big_img_path):
        xml_name = img_name.replace(".bmp", ".xml")
        xml_name = xml_name.replace(".jpg", ".xml")
        print(xml_name)
        img = cv2.imread(big_img_path + img_name)
        objs = minidom.parse(xml_path + xml_name).documentElement.getElementsByTagName('object')

        for index, obj in enumerate(objs):
            x1 = int(obj.getElementsByTagName('xmin')[0].firstChild.data)
            y1 = int(obj.getElementsByTagName('ymin')[0].firstChild.data)
            x2 = int(obj.getElementsByTagName('xmax')[0].firstChild.data)
            y2 = int(obj.getElementsByTagName('ymax')[0].firstChild.data)
            new_img = img[y1:y2, x1:x2]

            cv2.imwrite(esl_img_path + "{}_{}.jpg".format(index, img_name.split(".")[0]), new_img)

def resize_img():
    for img_name in os.listdir(esl_img_path):
        img = cv2.imread(esl_img_path + img_name)
        y, x, _ = img.shape
        new_y = int((img_size/x)*y)
        img_file = cv2.resize(img, (img_size, new_y))
        cv2.imwrite(barcode_img_path + "barcode_{}.jpg".format(img_name.split(".")[0]), img_file)

class WriteXml(object):
    def __init__(self, name):
        # sample.xml is .xml annotation file sample
        self.sample_xml = minidom.parse('./sample.xml')
        self.name = name
        self.root = self.sample_xml.documentElement
        self.filename_tag = self.root.getElementsByTagName('filename')
        self.filename_tag[0].firstChild.data = name
        sample_object = self.root.getElementsByTagName('object')[0]
        self.sample_object = minidom.parseString(sample_object.toxml()).documentElement

    def write_object(self, x1, y1, x2, y2, cls):
        before_node = self.root.childNodes[-1]
        obj = self.sample_object
                
        object_name = obj.getElementsByTagName("name")[0]
        object_name.firstChild.data = cls

        object_pose = obj.getElementsByTagName("pose")[0]
        object_pose.firstChild.data = "Unspecified"

        object_truncated = obj.getElementsByTagName("truncated")[0]
        object_truncated.firstChild.data = 1

        object_difficult = obj.getElementsByTagName("difficult")[0]
        object_difficult.firstChild.data = 0

        object_bndbox = obj.getElementsByTagName("bndbox")[0]
        xmin = object_bndbox.getElementsByTagName("xmin")[0]
        xmin.firstChild.data = x1

        ymin = object_bndbox.getElementsByTagName("ymin")[0]
        ymin.firstChild.data = y1

        xmax = object_bndbox.getElementsByTagName("xmax")[0]
        xmax.firstChild.data = x2

        ymax = object_bndbox.getElementsByTagName("ymax")[0]
        ymax.firstChild.data = y2

        obj = minidom.parseString(obj.toxml()).documentElement
        self.root.insertBefore( obj, before_node )

    def update_size(self, width, height):
        object_width = self.root.getElementsByTagName('width')[0]
        object_width.firstChild.data = width
        object_height = self.root.getElementsByTagName('height')[0]
        object_height.firstChild.data = height
    
    def save_xml(self, path):
        item = self.root.getElementsByTagName('object')[0]
        parent = item.parentNode
        parent.removeChild(item)
        
        self.root.writexml(open('{}{}.xml'.format(path, self.name), 'w'))

def get_position(bbox, height, width):
    print(bbox)
    x1, y1, x2, y2 = bbox
    x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
    center_x, center_y, width, height = x1*width, y1 * height, x2 * width, y2 * height
    x1 = int(center_x - width/2)
    y1 = int(center_y - height/2)
    x2 = int(center_x + width/2)
    y2 = int(center_y + height/2)+2
    return x1, y1, x2, y2
def sort_by_len(data):
    return data[-1]
def sort_by_width(data):
    return data[-1]
def sort_by_y(data):
    return data[1]

def change2xml(xml_path, img_path):
    # print(xml_path)
    try:
        os.system('rm {}*.xml'.format('./labels/'))
        os.system('rm labels.zip')
    except:
        pass
    if not os.path.exists('./labels'):
        os.mkdir('./labels')
    for txt_name in os.listdir(xml_path):
        if "xml" in txt_name: continue
        img_name = txt_name.replace(".txt", ".jpg")
        # print(img_name)
        img = cv2.imread(img_path + img_name)
        height, width, _ = img.shape
        xml = WriteXml(img_name.split(".")[0])
        xml.update_size(width = width, height = height)
        txt_file = open(xml_path + txt_name, 'r', encoding='utf-8')
        ele_array = list()

        for line in txt_file.readlines():
            elements = line.replace("\n", '').split(" ")
            if cfg["names"][int(elements[0])] == 'b': continue
            x1, y1, x2, y2 = get_position(elements[1:5], height, width)
            ele_array.append([x1, y1, x2, y2, cfg["names"][int(elements[0])], x2-x1])

        if len(ele_array) <= 1:
            for ele in ele_array:
                x1, y1, x2, y2, name, _ = ele
                xml.write_object(x1, y1, x2, y2, name)
            xml.save_xml(xml_path)
            continue
        ele_array.sort(key = sort_by_width, reverse=False)
        # base_ele = np.array(ele_array[0:int(len(ele_array)/2)]).astype(np.int16)
        # print(base_ele)
        # base_width = ele_array[0][-1]
        # print("base_width: ", base_width)
        ele_array.sort(key = sort_by_y, reverse=False)
        
        start_y = -200
        barcode_group = list()

        for ele in ele_array:
            if ele[1] > start_y + 20:
                if len(barcode_group) != 0:
                    barcode_group[-1].append(len(barcode_group[-1]))
                barcode_group.append([ele])
            else:
                barcode_group[-1].append(ele)
            start_y = ele[1]
        barcode_group[-1].append(len(barcode_group[-1]))
        # print(barcode_group)
        barcode_group.sort(key = sort_by_len, reverse=True)
        main_group = barcode_group[0]
        
        del main_group[-1]
        # print(main_group)

        for index, g in enumerate(barcode_group):
            for eles in g:
                if type(eles) == type(1): continue

                x1, y1, x2, y2, name, _ = eles
                #if base_width * 1.5 <  x2 - x1 and index == 0: continue
                xml.write_object(x1, y1, x2, y2, name)
                #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

        xml.save_xml(xml_path)

    os.system('mv {}*.xml ./labels'.format(xml_path))
    os.system('zip -D -r -q label.zip {}*.xml'.format('./labels/'))

        #cv2.imwrite("./data/vis/{}".format(img_name), img)
        # os.system("rm {}{}".format(xml_path, txt_name))

def rm_null(rootimgs,rootxmls):
    allusedxmls1 = []
    allusedxmls2 = []
    file_imgs = os.listdir(rootimgs)
    file_xmls = os.listdir(rootxmls)
    for file_name in file_imgs:
        file_name = file_name[:-4]
        allusedxmls1.append(file_name)

    for file_name in file_xmls:
        # print(file_name)
        if file_name[:-4] not in allusedxmls1:
            path = rootxmls + file_name
            os.remove(path)

    for file_name in file_xmls:
        file_name = file_name[:-4]
        allusedxmls2.append(file_name)

    for file_name in file_imgs:
        if file_name[:-4] not in allusedxmls2:
            path = rootimgs + file_name
            os.remove(path)


if __name__ == "__main__":
    #转换类别修改
    y = open("voc.yaml")

    cfg = yaml.load(y,Loader=yaml.FullLoader)
    #图像数据地址修改
    barcode_xml_path = '/home/xiehuaiqi/PycharmProjects/VOC/coal_estimation/SegmentationClass/'
    barcode_img_path = '/home/xiehuaiqi/PycharmProjects/VOC/coal_estimation/JPEGImages/'

    rm_null(barcode_img_path,barcode_xml_path)
    # change2xml(barcode_xml_path, barcode_img_path)




