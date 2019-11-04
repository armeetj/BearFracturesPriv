"""
author: @Armeet Jatyani (@xarmeetx)
2019
"""

import os
import shutil
import csv
import PIL 
from PIL import Image
import logging
logging.basicConfig(level=logging.DEBUG)

TRAIN_PATH = "engine/XR_HAND_dataset/train"
VALID_PATH = "engine/XR_HAND_dataset/valid"
ROWS=400
COLS=300

# clear dirs before extracting
for root, dirs, files in os.walk('engine/XR_HAND_dataset/'):
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
# remake dirs
os.mkdir(TRAIN_PATH)
os.mkdir(VALID_PATH)

print("continue? (y)/(n): ")
if(input()=="n"):
    exit();

def extract(images_path, train, resize): 
    logging.debug("Extracting data from: " + str(images_path) + "/n-> resize: " + str(resize))
    #extract validating data
    imgnumb = 1;
    imgnumsection = 1;
    if(train): 
        path = "engine/dataset/train/XR_HAND"
        logging.debug("-> extracting training data")
    else:
        path = "engine/dataset/valid/XR_HAND"
        logging.debug("-> extracting validation data")

    z = next(os.walk(path))[1]
    for patient in z:
        logging.debug (patient);
        finalPath = path + "/" + patient + "/" + next(os.walk(path + "/" + patient))[1][0]
        finalResult = "";
        if "positive" in next(os.walk(path + "/" + patient))[1][0]:
            finalResult = "1";
        else:
            finalResult = "0";
        logging.debug(finalPath);
        images = [i[2] for i in os.walk(finalPath)]
        for t in images:
            for f in t:
                logging.debug("    reading: " + f)
                logging.debug("    writing: " + patient + "_image" + str(imgnumb )+ "_" + str(imgnumsection) + ".png")
                shutil.copy((finalPath+ "/" + f), images_path + "/" + patient +"_image"+ str(imgnumb) + "_" + str(imgnumsection) + ".png", follow_symlinks=True)
            
                #resize image if true
                if(resize):
                    img = Image.open(images_path + "/" + patient +"_image"+ str(imgnumb) + "_" + str(imgnumsection) + ".png")
                    # img.thumbnail((ROWS, COLS), Image.ANTIALIAS)
                    img = img.resize((COLS, ROWS), Image.ANTIALIAS)
                    img.save(images_path + "/" + patient +"_image"+ str(imgnumb) + "_" + str(imgnumsection) + ".png")
                
                #copy label
                if finalResult=="0":
                    shutil.copy("engine/XR_HAND_dataset/result0.txt", images_path + "/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
                else:
                    shutil.copy("engine/XR_HAND_dataset/result1.txt", images_path + "/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
                imgnumsection = imgnumsection + 1;

        imgnumsection = 1;
        imgnumb = imgnumb + 1;

#extract training and validating data
extract(TRAIN_PATH, True, True)
extract(VALID_PATH, False, True)