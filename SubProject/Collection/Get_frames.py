import os
import cv2
import shutil

# Video source address
videos_src_path = '..\Video'
frame_sv_path = '..\Frames'

# Frame saving address
if not os.path.exists(frame_sv_path):
    os.makedirs(frame_sv_path)
else:
    shutil.rmtree(frame_sv_path)
    os.makedirs(frame_sv_path)

# Return all video names in the source video folder
videos = os.listdir(videos_src_path)

for each_video in videos:
    # Get the name of each video
    each_video_name, _ = each_video.split('.')

    # Create a directory to save image frames
    os.mkdir(frame_sv_path + '/' + each_video_name)

    # Get the full path where the images are saved
    # The image frames for each video are in a folder with the video name as the file name
    each_video_save_full_path = os.path.join(frame_sv_path, each_video_name) + '/'

    # Get the full path to each video
    each_video_full_path = os.path.join(videos_src_path, each_video)

    # read video
    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    frame_rate = 1
    while True:
        ret, frame = cap.read()
        if ret:
            if frame_count % frame_rate == 0:
                print("Start capturing video frame: " + str(frame_count))
                cv2.imwrite(each_video_save_full_path + "%02d.jpg" % frame_count, frame)
            frame_count += 1
            cv2.waitKey(0)
        else:
            print("All frames are saved")
            break
    cap.release()
