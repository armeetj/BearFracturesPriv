"""
author: @Armeet Jatyani (@xarmeetx)
"""

from __future__ import absolute_import, division, print_function, unicode_literals
from PIL import Image  

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
import os

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
test_labels = []

#read in all training and validating images to raw arrays
train_folder_raw_data = [i[2] for i in os.walk(TRAIN_PATH)]
for folder in train_folder_raw_data:
    print(folder)
    for f in folder:
        print(f)
        if ".png" in f:
            raw_train_images.append(f);
        else:
            with open (TRAIN_PATH + "/" + f, "r") as temp_label:
                data=str(temp_label.readlines()[0])
                train_labels.append(data);
