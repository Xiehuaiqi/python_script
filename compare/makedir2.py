
import os

def text_save(content,filename,mode='a'):
    # Try to save a list variable in txt file.
    file = open(filename, mode)
    for i in range(len(content)):
        file.write(str(content[i])+'\n')
    file.close()

file_dir = "/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/JPEGImages"

def get_files(file_dir):

    namelist = []
    for file in os.listdir(file_dir):
        name = file.split('.')
        namelist.append(name[0])
    return(namelist)
def main():
    a=get_files(file_dir)
    return a
    #text_save(a, '/home/zx/desktop/xiehuaiqi/datasets/CaltechPestrian/JEPT.txt')