import xml.etree.ElementTree as ET

t =
tree = ET.parse("/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/img-000-0.xml")
root = tree.getroot()
print root[5][1][0].text


