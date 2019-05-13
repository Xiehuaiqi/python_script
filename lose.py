import os
from PIL import Image
num = 1
path = "/home/zx/desktop/Yawning/"
for filename in os.listdir(r"/home/zx/desktop/Yawning"):
    print(num)
    num+=1
    print(filename)
    #os.system("nautilus " + path + filename)
    # for j in os.listdir(r"/home/zx/desktop/Yawning/"+filename):
    #     print()