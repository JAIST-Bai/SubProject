import os
import cv2
import numpy as np
import mediapipe as mp
from tqdm import tqdm

mp_holistic = mp.solutions.holistic  # Holistic model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # Image is no longer writeable
    results = model.process(image)  # Make prediction
    image.flags.writeable = True  # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR CONVERSION RGB 2 BGR
    return image, results


def draw_styled_landmarks(image, results):
    # Draw face connections
    # mp_drawing.draw_landmarks(
    #    image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
    #   mp_drawing.DrawingSpec(color=(80, 110, 10), thickness=1, circle_radius=1),
    #    mp_drawing.DrawingSpec(color=(80, 256, 121), thickness=1, circle_radius=1)
    # )

    # Draw pose connections
    mp_drawing.draw_landmarks(
        image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0, 0, 185), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(0, 165, 255), thickness=2, circle_radius=1)
    )

    # Draw left hand connections
    mp_drawing.draw_landmarks(
        image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0, 0, 185), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(50, 205, 50), thickness=2, circle_radius=1)
    )

    # Draw right hand connections
    mp_drawing.draw_landmarks(
        image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(0, 0, 185), thickness=1, circle_radius=1),
        mp_drawing.DrawingSpec(color=(209, 206, 0), thickness=2, circle_radius=1)
    )


def extract_keypoints(results):
    # face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() \
    # if results.face_landmarks else np.zeros(468 * 3)
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() \
        if results.pose_landmarks else np.zeros(33 * 4)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() \
        if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() \
        if results.right_hand_landmarks else np.zeros(21 * 3)
    return np.concatenate([pose, lh, rh])


No_sequences = 30
frame_length = 30
DATA_PATH = os.path.join('gloss_data')


def BEAUTIFUL():
    gloss = np.array(['BEAUTIFUL'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_BEAUTIFUL.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()

def HOT():
    gloss = np.array(['HOT'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_HOT.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()


def LIKE():
    gloss = np.array(['LIKE'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_LIKE.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()

def SUBJECT_I():
    gloss = np.array(['SUBJECT_I'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_SUBJECT_I.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()


def SUMMER():
    gloss = np.array(['SUMMER'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_SUMMER.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()

def SWIM():
    gloss = np.array(['SWIM'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_SWIM.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()

def WINTER():
    gloss = np.array(['WINTER'])
    for sign in gloss:
        for sequence in range(No_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))
            except:
                pass
    cap = cv2.VideoCapture('..\Video\M_WINTER.mp4')
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for sign in gloss:
            for sequence in tqdm(range(No_sequences), ncols=80):
                for frame_num in range(frame_length):
                    ret, frame = cap.read()
                    if not ret:
                        break
                    image, results = mediapipe_detection(frame, holistic)
                    draw_styled_landmarks(image, results)
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, sign, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
    cap.release()
    cv2.destroyAllWindows()


def collection_choose():
    import sys
    path_str = input \
        ('''
                1.BEAUTIFUL
                2.LIKE
                3.SUBJECT_I
                4.SNOW
                5.SUMMER
                6.SWIM
                7.WINTER
                8.ALL
                9.EXIT----Do nothing and exit
                Please enter the Gloss video you want to collect: ''')
    if path_str == 'BEAUTIFUL':
        BEAUTIFUL()
        collection_choose()
    elif path_str == 'HOT':
        HOT()
        collection_choose()
    elif path_str == 'LIKE':
        LIKE()
        collection_choose()
    elif path_str == 'SUBJECT_I':
        SUBJECT_I()
        collection_choose()
    elif path_str == 'SUMMER':
        SUMMER()
        collection_choose()
    elif path_str == 'SWIM':
        SWIM()
        collection_choose()
    elif path_str == 'WINTER':
        WINTER()
        collection_choose()
    elif path_str == 'ALL':
        BEAUTIFUL()
        HOT()
        LIKE()
        SUBJECT_I()
        SUMMER()
        SWIM()
        WINTER()
        collection_choose()
    elif path_str == 'EXIT':
        sys.exit()
    else:
        print('''[0;31mError command! Please Re-enter: ''')
        collection_choose()


if __name__ == "__main__":
    collection_choose()
