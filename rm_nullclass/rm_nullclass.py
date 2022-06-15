import xml.etree.ElementTree as ET
import glob,os
xml_path = '/home/xiehuaiqi/Pictures/data4/data4/*.xml'

for image_file in glob.glob(xml_path):
    # print(image_file)

    tree = ET.parse(image_file)
    root = tree.getroot()

    num = 0
    for childs in root:
        if childs.tag=='object':
            num += 1

    if num == 0:

        print(image_file)
