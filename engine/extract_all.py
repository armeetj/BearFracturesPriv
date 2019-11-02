import os
import shutil
import csv


# clear dirs before extracting
for root, dirs, files in os.walk('engine/XR_HAND_dataset/'):
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
# remake dirs
os.mkdir("engine/XR_HAND_dataset/train")
os.mkdir("engine/XR_HAND_dataset/valid")

print("Continue? (y)/(n): ")
if(input()=="n"):
    exit();

#extract training data
imgnumb = 1;
imgnumsection = 1;
path = "engine/dataset/train/XR_HAND"

z = next(os.walk(path))[1]
for patient in z:
    print (patient);
    finalPath = path + "/" + patient + "/" + next(os.walk(path + "/" + patient))[1][0]
    finalResult = "";
    if "positive" in next(os.walk(path + "/" + patient))[1][0]:
        finalResult = "1";
    else:
        finalResult = "0";
    print(finalPath);
    images = [i[2] for i in os.walk(finalPath)]
    for t in images:
        for f in t:
            print("reading: " + f)
            print("writing: " + patient + "_image" + str(imgnumb )+ "_" + str(imgnumsection) + ".png")
            shutil.copy((finalPath+ "/" + f), "engine/XR_HAND_dataset/train/" + patient +"_image"+ str(imgnumb) + "_" + str(imgnumsection) + ".png", follow_symlinks=True)
            imgnumsection = imgnumsection + 1;

            if finalResult=="0":
                shutil.copy("engine/XR_HAND_dataset/result0.txt", "engine/XR_HAND_dataset/train/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
            else:
                shutil.copy("engine/XR_HAND_dataset/result1.txt", "engine/XR_HAND_dataset/train/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
    imgnumsection = 1;
    imgnumb = imgnumb + 1;

#extract validating data
imgnumb = 1;
imgnumsection = 1;
path = "engine/dataset/valid/XR_HAND"

z = next(os.walk(path))[1]
for patient in z:
    print (patient);
    finalPath = path + "/" + patient + "/" + next(os.walk(path + "/" + patient))[1][0]
    finalResult = "";
    if "positive" in next(os.walk(path + "/" + patient))[1][0]:
        finalResult = "1";
    else:
        finalResult = "0";
    print(finalPath);
    images = [i[2] for i in os.walk(finalPath)]
    for t in images:
        for f in t:
            print("reading: " + f)
            print("writing: " + patient + "_image" + str(imgnumb )+ "_" + str(imgnumsection) + ".png")
            shutil.copy((finalPath+ "/" + f), "engine/XR_HAND_dataset/valid/" + patient +"_image"+ str(imgnumb) + "_" + str(imgnumsection) + ".png", follow_symlinks=True)
            imgnumsection = imgnumsection + 1;

            if finalResult=="0":
                shutil.copy("engine/XR_HAND_dataset/result0.txt", "engine/XR_HAND_dataset/valid/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
            else:
                shutil.copy("engine/XR_HAND_dataset/result1.txt", "engine/XR_HAND_dataset/valid/" + patient +"_result"+ str(imgnumb) + "_" + str(imgnumsection) + ".txt", follow_symlinks=True)
    imgnumsection = 1;
    imgnumb = imgnumb + 1;