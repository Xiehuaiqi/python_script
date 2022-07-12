import os

path = './'
# l = os.listdir(path)
# print(sorted(l))
# exit()
for num,i in enumerate(sorted(os.listdir(path))):
    print(i,num)
    if i.split('.')[-1] == 'mp4':
        # os.rename(path+i,path+str(num)+'.mp4')
        # os.system('mv ' + path + i + ' ' + path + i.split('.')[0] + '.mp4')
        with open("filelist.txt", 'a+') as f:
            f.write('file \'' + i+ '\'' + '\n')
f.close()
#ffmpeg -f concat -safe 0 -i mylist.txt -c copy myvideo.mp4
