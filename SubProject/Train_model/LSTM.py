import numpy as np
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import TensorBoard, ReduceLROnPlateau
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

logs = os.path.join('..\Model')
Tensorboard_callback = [TensorBoard(log_dir=logs), ReduceLROnPlateau(factor=0.1, patience=5)]

No_sequences = 30
sequence_length = 30

DATA_PATH = os.path.join('..\gloss_data')

gloss = np.array(['BEAUTIFUL', 'HOT', 'LIKE', 'SUBJECT_I', 'SUMMER', 'SWIM', 'WINTER'])


label_map = {label: num for num, label in enumerate(gloss)}
sequences, labels = [], []
for sign in gloss:
    for sequence in range(No_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, sign, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[sign])

X = np.array(sequences)
Y = to_categorical(labels).astype(int)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)


model = Sequential()
model.add((LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 258))))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(32, activation='relu'))
model.add(Dense(gloss.shape[0], activation='softmax'))
model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, Y_train, validation_split=0.2, epochs=80, callbacks=[Tensorboard_callback])
model.summary()
model.save('gloss.h5')


history_dict = history.history
print(history_dict.keys())

plt.figure(1)
plt.subplot(211)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='lower right')

plt.subplot(212)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Training', 'Validation'], loc='upper right')

plt.tight_layout()
plt.show()
