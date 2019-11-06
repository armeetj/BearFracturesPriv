"""
author: @Armeet Jatyani (@xarmeetx)
2019
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import Image  

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib import image
from matplotlib import pyplot

#constants
ROWS=400
COLS=400
CHANNELS=1
EPOCHS=5
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 8
TRAIN_PATH = "engine/XR_HAND_dataset/small_train"
VALID_PATH = "engine/XR_HAND_dataset/small_valid"
#TRAIN_PATH = "engine/XR_HAND_dataset/train"
#VALID_PATH = "engine/XR_HAND_dataset/valid"
# Define the number of classes
NUM_CLASSES = 2
classes = {0 : "normal" , 1 : "broken"}

#PNG files
raw_train_images=[]
raw_valid_images=[]

#numpy
train_images=[]
valid_images=[]

#labels
train_labels = []
valid_labels = []

def read_data(images, labels, path):
    folder_raw_data = [i[2] for i in os.walk(path)]
    for folder in folder_raw_data:
        for f in folder:
            if ".png" in f:
                images.append(image.imread(path + "/" + f));
            else:
                with open (path + "/" + f, "r") as temp_label:
                    data=str(temp_label.readlines()[0])
                    labels.append(data);
def format_data():
    train_image_generator = ImageDataGenerator(rescale=1./255)
    valid_image_generator = ImageDataGenerator(rescale=1./255)
    train_images = train_image_generator.flow_from_directory(batch_size=TRAIN_BATCH_SIZE,
                                                           directory=TRAIN_PATH,
                                                           shuffle=True,
                                                           target_size=(ROWS, COLS),
                                                           class_mode='binary')
    valid_images = valid_image_generator.flow_from_directory(batch_size=VALID_BATCH_SIZE,
                                                           directory=VALID_PATH,
                                                           target_size=(ROWS, COLS),
                                                           class_mode='binary')

def plot(z):
    plt.figure(figsize=(3,3))
    for i in range(z):
        plt.subplot(int(sqrt(z))+1,int(sqrt(z))+1,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i])
        plt.xlabel(classes[int(train_labels[i])])
    plt.show()

# read_data(train_images, train_labels, TRAIN_PATH)
# read_data(valid_images, valid_labels, VALID_PATH)   
format_data();       

model = Sequential([
    Conv2D(16, 3, padding='same', activation='relu', input_shape=(ROWS, COLS ,3)),
    MaxPooling2D(),
    Conv2D(32, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Conv2D(64, 3, padding='same', activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
model.summary()

history = model.fit_generator(
    train_images,
    steps_per_epoch=TRAIN_BATCH_SIZE // TRAIN_BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=valid_images,
    validation_steps=VALID_BATCH_SIZE // VALID_BATCH_SIZE
)

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(EPOCHS)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

valid_loss, valid_acc = model.evaluate(valid_images,  valid_labels, verbose=2)
print("valid_acc: " + str(valid_acc))


print("\nWritten by Armeet Singh Jatyani 2019")
