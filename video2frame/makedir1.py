#coding:utf-8
import os

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

# file_dir = "/home/zx/desktop/华谊化工/"

def get_files(file_dir):

    namelist = []
    for file in os.listdir(file_dir):
        name = file.split('.')
        namelist.append(name[0])
    return(namelist)
def main(file_dir):
    a=get_files(file_dir)
    return a
#     text_save(a, '/home/zx/desktop/华谊化工/Annotations.txt')
#
# if __name__ == '__main__':
#     main(file_dir)