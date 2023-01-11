import cv2
import glob
import shutil
from moviepy.editor import *


def resize(img_array, align_mode):
    _height = len(img_array[0])
    _width = len(img_array[0][0])
    for i in range(1, len(img_array)):
        img = img_array[i]
        height = len(img)
        width = len(img[0])
        if align_mode == 'smallest':
            if height < _height:
                _height = height
            if width < _width:
                _width = width
        else:
            if height > _height:
                _height = height
            if width > _width:
                _width = width

    for i in range(0, len(img_array)):
        img1 = cv2.resize(img_array[i], (_width, _height), interpolation=cv2.INTER_CUBIC)
        img_array[i] = img1

    return img_array, (_width, _height)


def images_to_video(path):
    img_array = []
    for filename in glob.glob(path + '/*.jpg'):
        img = cv2.imread(filename)
        if img is None:
            print(filename + " is error!")
            continue
        img_array.append(img)

    img_array, size = resize(img_array, 'largest')
    fps = 40
    if not os.path.exists("..\Video"):
        os.makedirs("..\Video")
    out = cv2.VideoWriter('..\Video\data.mp4v', cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()



def BEAUTIFUL():
    path = "..\Frames\BEAUTIFUL"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\BEAUTIFUL.mp4v")

    for x in range(0, 30):
        a = "..\Video" + "BEAUTIFUL" + str(x) + ".mp4v"
        shutil.copy2("..\Video\BEAUTIFUL.mp4v", a)

    src_path = "..\Video"
    filter_name = "BEAUTIFUL"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_BEAUTIFUL.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)

def HOT():
    path = "..\Frames\HOT"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\HOT.mp4v")

    for x in range(0, 40):
        a = "..\Video" + "HOT" + str(x) + ".mp4v"
        shutil.copy2("..\Video\HOT.mp4v", a)

    src_path = "..\Video"
    filter_name = "HOT"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_HOT.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            

def LIKE():
    path = "..\Frames\LIKE"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\LIKE.mp4v")

    for x in range(0, 40):
        a ="..\Video" + "LIKE" + str(x) + ".mp4v"
        shutil.copy2("..\Video\LIKE.mp4v", a)

    src_path = "..\Video"
    filter_name = "LIKE"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_LIKE.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def SUBJECT_I():
    path = "..\Frames\SUBJECT_I"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\SUBJECT_I.mp4v")

    for x in range(0, 40):
        a = "..\Video" + "SUBJECT_I" + str(x) + ".mp4v"
        shutil.copy2("..\Video\SUBJECT_I.mp4v", a)

    src_path = "..\Video"
    filter_name = "SUBJECT_I"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_SUBJECT_I.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            
            
def SUMMER():
    path = "..\Frames\SUMMER"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\SUMMER.mp4v")

    for x in range(0, 40):
        a = "..\Video" + "SUMMER" + str(x) + ".mp4v"
        shutil.copy2("..\Video\SUMMER.mp4v", a)

    src_path = "..\Video"
    filter_name = "SUMMER"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_SUMMER.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def SWIM():
    path = "..\Frames\SWIM"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\SWIM.mp4v")

    for x in range(0, 40):
        a = "..\Video" + "SWIM" + str(x) + ".mp4v"
        shutil.copy2("..\Video\SWIM.mp4v", a)

    src_path = "..\Video"
    filter_name = "SWIM"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_SWIM.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)

            
def WINTER():
    path = "..\Frames\WINTER"
    images_to_video(path)
    os.rename("..\Video\data.mp4v", "..\Video\WINTER.mp4v")

    for x in range(0, 40):
        a = "..\Video" + "WINTER" + str(x) + ".mp4v"
        shutil.copy2("..\Video\WINTER.mp4v", a)

    src_path = "..\Video"
    filter_name = "WINTER"
    files = []
    for dir_name, dir_names, filenames in os.walk(src_path):
        for sub_dirname in dir_names:
            files.append(os.path.join(dir_name, sub_dirname))
        for filename in filenames:
            if filter_name in filename:
                files.append(os.path.join(dir_name, filename))
    clips = []
    for i in files:
        clips.append(VideoFileClip(i))
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("..\Extened_video\M_WINTER.mp4", codec="libx264")
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def path_choose():
    import sys
    path_str = input \
        ('''\033[0;33m
                1.BEAUTIFUL
                2.LIKE
                3.SUBJECT_I
                4.SNOW
                5.SUMMER
                6.SWIM
                7.WINTER
                8.ALL
                9.EXIT----Do nothing and exit
                Please enter the Gloss frames you want to merge: \033[0m''')
    if path_str == 'BEAUTIFUL':
        if os.path.exists("..\Video\M_BEAUTIFUL.mp4"):
            os.remove("..\Video\M_BEAUTIFUL.mp4")
            BEAUTIFUL()
            path_choose()
    elif path_str == 'HOT':
        if os.path.exists("..\Video\M_HOT.mp4"):
            os.remove("..\Video\M_HOT.mp4")
            HOT()
            path_choose()
    elif path_str == 'LIKE':
        if os.path.exists("..\Video\M_LIKE.mp4"):
            os.remove("..\Video\M_LIKE.mp4")
            LIKE()
            path_choose()
    elif path_str == 'SUBJECT_I':
        if os.path.exists("..\Video\M_SUBJECT_I.mp4"):
            os.remove("..\Video\M_SUBJECT_I.mp4")
            SUBJECT_I()
            path_choose()
    elif path_str == 'SUMMER':
        if os.path.exists("..\Video\M_SUMMER.mp4"):
            os.remove("..\Video\M_SUMMER.mp4")
            SUMMER()
            path_choose()
    elif path_str == 'SWIM':
        if os.path.exists("..\Video\M_SWIM.mp4"):
            os.remove("..\Video\M_SWIM.mp4")
            SWIM()
            path_choose()
    elif path_str == 'WINTER':
        if os.path.exists("..\Video\M_WINTER.mp4"):
            os.remove("..\Video\M_WINTER.mp4")
            WINTER()
            path_choose()
    elif path_str == 'ALL':
        BEAUTIFUL()
        HOT()
        LIKE()
        SUBJECT_I()
        SUMMER()
        SWIM()
        WINTER()
        path_choose()
    elif path_str == 'EXIT':
        sys.exit()
    else:
        print("\033[0;31mError command! Please Re-enter:\033[0m")
        path_choose()


if __name__ == "__main__":
    path_choose()
