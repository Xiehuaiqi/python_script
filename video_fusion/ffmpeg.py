import os

command = 'ffmpeg -f concat -i filelist.txt -safe 0 -c copy output_set.mp4'
os.system(command)

