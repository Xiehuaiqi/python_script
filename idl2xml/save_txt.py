#coding:utf-8
source_path = "/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/yimg-000-0.xml"
goal_path = "/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-Brussels/annotation/"

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

ano = open("/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-MotionPairs/additional-negative-bootstrap/annotation.idl")
lines = ano.readlines()
num = 0
namelist = []
for line in lines:
    if ":" in line:
        num += 1
        #以冒号为标记分割
        line = line.split(":")
        #print line[0],line[1]

        name = eval(line[0]).split(".")
        # 取出标记坐标
        print name[0]
        namelist.append(name[0])
print len(namelist)
text_save(namelist, '/home/zx/desktop/xiehuaiqi/datasets/pedestrainsETH/TUD-MotionPairs/additional-negative-bootstrap/Annotations.txt')