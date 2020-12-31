import cv2
import os
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import os
import os.path
from os import path
import query

def saveHisto():
    fsWrite = cv2.FileStorage("histograms.txt", cv2.FileStorage_WRITE )
    if path.exists("gallery/.DS_Store"):
        os.remove("gallery/.DS_Store")
    image_names = os.listdir("gallery/")

    for filename in image_names:
        image=cv2.imread(f"gallery/{filename}")
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        hist = cv2.calcHist([image],[0, 1, 2], None,[8, 8, 8],[0, 256, 0, 256, 0, 256]) 
        hist = cv2.normalize(hist, hist).flatten()
        nomeFile = os.path.splitext(filename)[0]
        fsWrite.write(f'histogram_{nomeFile}' ,hist)

    print("Salvataggio eseguito")
    fsWrite.release()

