import os


def grab_images_from_video(video_path="", save_dir="", filename=""):
    # -r 一秒截取多少张
    # -vf fps=1/20 每隔20秒截取一张
    os.system(
        'ffmpeg -i ' + video_path + ' -f image2  -q:v 2 -vf fps=fps=1/2 ' + save_dir + '/' + filename + '_image-%4d.jpg')


video_path = '/home/xiehuaiqi/Videos/vlc_video_recording/'
save_path = '/home/xiehuaiqi/Pictures/皮带跑偏0610/'
for name in os.listdir(video_path):
    print(name)
    file = name.split('.')[0]
    grab_images_from_video(video_path + name, save_path, file)
