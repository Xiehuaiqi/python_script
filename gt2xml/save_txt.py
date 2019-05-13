#coding:utf-8
source_path = "/home/zx/PycharmProjects/compare/gt2xml/img-001-2.xml"
goal_path = "/home/zx/博士VOC/MOT17VOC/Annotations/"

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

ano = open("/home/zx/博士VOC/train/MOT17-02/gt/gt.txt")
lines = ano.readlines()
num = 0
namelist = []
for line in lines:
    num += 1
    #以冒号为标记分割
    line = line.split(",")
    # print line[0],line[1]
    if line[0]
    name = eval(line[0]).split(".")
    # 取出标记坐标
    print name[0]
    namelist.append(name[0])

print len(namelist)
text_save(namelist, '/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-MotionPairs/additional-negative-bootstrap/Annotations.txt')