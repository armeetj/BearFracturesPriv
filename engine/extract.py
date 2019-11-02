import shutil
import os
import csv
    
    
imgnumb = 1;
with open('engine/train_hand_paths.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
        shutil.copy((row[0]+"image1.png"), "engine/XR_HAND_dataset/train/image"+ str(imgnumb) + ".png", follow_symlinks=True)

        if row[1]=="0":
            shutil.copy("engine/XR_HAND_dataset/result0.txt", "engine/XR_HAND_dataset/train/result"+ str(imgnumb) + ".txt", follow_symlinks=True)
        else:
            shutil.copy("engine/XR_HAND_dataset/result1.txt", "engine/XR_HAND_dataset/train/result"+ str(imgnumb) + ".txt", follow_symlinks=True)
       
        imgnumb = imgnumb+1;

imgnumb = 1;
with open('engine/valid_hand_paths.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(row)
        shutil.copy((row[0]+"image1.png"), "engine/XR_HAND_dataset/valid/image"+ str(imgnumb) + ".png", follow_symlinks=True)

        if row[1]=="0":
            shutil.copy("engine/XR_HAND_dataset/result0.txt", "engine/XR_HAND_dataset/valid/result"+ str(imgnumb) + ".txt", follow_symlinks=True)
        else:
            shutil.copy("engine/XR_HAND_dataset/result1.txt", "engine/XR_HAND_dataset/valid/result"+ str(imgnumb) + ".txt", follow_symlinks=True)
       
        imgnumb = imgnumb+1;