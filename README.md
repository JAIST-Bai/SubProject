### SubProject

In this project, I implemented the process of sign language recognition and translation from video to text based on skeletal coordinates and Fill Mask.

The sections of the document are as follows.

 1. Folder-Collection: Used to pre-process the video to collect skeletal data.
 
(1). Get_frames.py: Get continuous video frames.

(2). Generation.py: expand the video length to meet the acquisition read length requirement.

(3). Keypoints.py: based on mediapipe for skeletal data collection, containing three categories of data: pose, left hand and right hand.


 2. Folder-Frames: Used to store the continuous video frame data generated by the Get_frames.py file. After that we need to manually filter the keyframes and remove the start and end frames of the action. For each action I have selected 20 continuous images as keyframes.

 3. Folder-Extened_video: Used to store the expanded video.

 4. Folder-gloss_data: It is used to store the collected skeletal data and contains 7 words: BEAUTIFUL, HOT, LIKE, SUBJECT_I, SUMMER, SWIM, WINTER. The movements are referenced from the German Deaf Sign Language Corpus (DGS) and were recorded by myself. Due to personal privacy reasons, the code repository does not include video data, I apologize for this.
 
 Please see reference for DGS links.

 5. Folder-Train_model: Used to store the training weights and training log files. It mainly includes.
 
(1). LSTM.py: all skeletal data will be fed into the classical long and short-term memory model for training. I did not make many changes to the structure of this network, and it performs well enough for the data in this project.

(2). Best_gloss.h5: This is the best result I have ever trained, and based on this I continue with the text processing task.

(3). Best_Results.png: This is the Acc and Loss training graph generated by LSTM.py.

 6. Folder-Test_video: Used to store test videos. There are 4 continuous sign language videos with the following sentences (without correction): "I LIKE SUMMER WINTER", "SUMMER HOT", "WINTER BEAUTIFUL", "I LIKE SWIM SUMMER". Also they were recorded by myself and not added to the code repository.

 7. main.py: used to test the Test_video data, and the result is output as text.
 
 Note: Please run main.py with the command "$ python main.py > ***.txt"
 

 8. Folder-Sentences_logs: Used to store the text results generated after the test. 
 
(1). Clear.py: Perform text preprocessing, which will eventually get Sentences.txt in Fill_mask.

 9. Folder-Fill_mask: contains processing commands and test text with <mask>. 
 
(1). Fill_Mask.py: used to run the Fill_Mask prediction task on the contents of Sentences.txt to fill in the missing sentence components of the direct sign language text to make it more natural language expression.
  
 Note: Please run the Fill_Mask.py code in Powershell
  
  
 10. Result_mark.png：Final text result. The results and probabilities of each of the four sentences are marked with four different colors.
  
 11. Requirements.txt: for installing dependencies

 
 ### References:
 mediapipe: 
 https://github.com/google/mediapipe
 
 
 Fill_Mask Model (roberta-base): 
 https://huggingface.co/roberta-base?text=Paris+is+the+%3Cmask%3E+of+France
 
 
 DGS: https://www.sign-lang.uni-hamburg.de/meinedgs/ling/start_en.html


### Evaluation
 
The LSTM training part performed well and was able to achieve accurate recognition.

 ![Best_Results](https://user-images.githubusercontent.com/106440647/211692153-fe663c73-971f-4f04-9712-dd18c79492e4.png)


The Text text part "SUMMER HOT" has a low score (see the yellow annotated part of Result.png), but the other three sentences can achieve Fill_Mask accurately.
 
 ![image](https://user-images.githubusercontent.com/106440647/211692211-9b51204b-dd68-46bb-b480-fa0859512a50.png)


