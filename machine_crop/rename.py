import os

below_path = '/home/xhq/VOC/machine/48cm/'
middle_path = '/home/xhq/VOC/machine/102cm/'
on_path = '/home/xhq/VOC/machine/154.5cm/'

tmp = list()
for i in os.listdir(path):
    n = i.split('.')[0].split('G')[-1]
    os.system('mv {} {}'.format(path + i,path+ n +'.jpeg'))
    #i = i.split('.')[0].split('G')[-1]
    #tmp.append(int(i))
    
#tmp.sort()
#print(tmp)
