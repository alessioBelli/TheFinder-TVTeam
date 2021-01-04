import cv2
import os
import os.path
from os import path
import math


def saveHisto():
    fsWrite = cv2.FileStorage("histograms.txt", cv2.FileStorage_WRITE )
    if path.exists("gallery/.DS_Store"):
        os.remove("gallery/.DS_Store")
    image_names = os.listdir("gallery/")

    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]
        image=cv2.imread(f"gallery/{filename}")
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        windowsize_r = math.ceil(image.shape[0]/2)
        windowsize_c = math.ceil(image.shape[1]/2)

        countc=0
        countr=0
        for r in range(0,image.shape[0] , windowsize_r):
            for c in range(0,image.shape[1], windowsize_c):
                window = image[r:r+windowsize_r,c:c+windowsize_c]
                hist = cv2.calcHist([window],[0, 1, 2], None,[8, 8, 8],[0, 256, 0, 256, 0, 256])
                hist = cv2.normalize(hist, hist).flatten()
                fsWrite.write(f'histogram_{countr}_{countc}_{nomeFile}' ,hist)
                countc+= 1
            countr+=1
            countc=0

    print("Salvataggio eseguito")
    fsWrite.release()

