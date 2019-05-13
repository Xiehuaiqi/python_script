#coding:utf-8
import os

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

file_dir = "/home/zx/data/VOCdevkit/VOC2012/JPEGImages"

def get_files(file_dir):

    namelist = []
    for file in os.listdir(file_dir):
        name = file.split('.')[0]
        namelist.append(name)
    return namelist
def main():
    a = get_files(file_dir)
    # print a
    #return a
    text_save(a, '/home/zx/data/VOCdevkit/VOC2012/jpg.txt')
if __name__ == '__main__':
    main()
