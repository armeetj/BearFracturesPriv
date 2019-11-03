"""
author: @Armeet Jatyani (@xarmeetx)
2019
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import Image  

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import os

from matplotlib import image
from matplotlib import pyplot

#constants
ROWS=400
COLS=400
CHANNELS=1
EPOCHS=10
TRAIN_PATH = "engine/XR_HAND_dataset/train"
VALID_PATH = "engine/XR_HAND_dataset/valid"

# Define the number of classes
NUM_CLASSES = 2
classes = {'normal' : 0 , 'broken' : 1}

#PNG files
raw_train_images=[]
raw_valid_images=[]

#numpy
train_images=[]
valid_images=[]

#labels
train_labels = []
valid_labels = []

#read in all training and validating images to raw arrays
train_folder_raw_data = [i[2] for i in os.walk(TRAIN_PATH)]
for folder in train_folder_raw_data:
    for f in folder:
        if ".png" in f:
            print(f)
            train_images.append(image.imread(TRAIN_PATH + "/" + f));
            img = Image.open(TRAIN_PATH + "/" + f)
            print("read and converted png")
            # create a thumbnail and preserve aspect ratio
            img.thumbnail((ROWS,COLS))
            print("resized image")
        else:
            with open (TRAIN_PATH + "/" + f, "r") as temp_label:
                data=str(temp_label.readlines()[0])
                train_labels.append(data);

valid_folder_raw_data = [i[2] for i in os.walk(VALID_PATH)]
for folder in valid_folder_raw_data:
    for f in folder:
        if ".png" in f:
            print(f)
            valid_images.append(image.imread(VALID_PATH + "/" + f));
            img = Image.open(VALID_PATH + "/" + f)
            print("read and converted png")
            # create a thumbnail and preserve aspect ratio
            img.thumbnail((ROWS,COLS))
            print("resized image")
        else:
            with open (VALID_PATH + "/" + f, "r") as temp_label:
                data=str(temp_label.readlines()[0])
                valid_labels.append(data);

print(train_images)
print(valid_images)
train_labels = np.array(train_labels)
valid_labels = np.array(valid_labels)
print(train_labels)
print(valid_labels)

""" print("train shape")
print (train_images.shape)
print("valid shape")
print (valid_images.shape) """
""" 
# Normalize pixel values to be between 0 and 1
train_images, valid_images = train_images / 255.0, valid_images / 255.0

print(train_images) """

print("Written by Armeet Singh Jatyani 2019")
