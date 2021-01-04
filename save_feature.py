from feature_extractor import FeatureExtractor
from pathlib import Path
from PIL import Image
import numpy as np
import os
import sys


def creazioneFeature():
    fe = FeatureExtractor()
    if os.path.isdir("./features") == True:
        print("Directory già presente")
    else:
        os.mkdir("./features")
    image_names = os.listdir("gallery/")

 
    cont = 0
    for filename in image_names:
        cont = cont+1
        if cont % 10 == 0:
            sys.stdout.write('\r' + "Le immagini elaborate sono attualmente : " + str(cont) + "/" + str(len(image_names)))
            sys.stdout.flush() # important
        nomeFile = os.path.splitext(filename)[0]
        feature = fe.extract(img=Image.open(f"gallery/{nomeFile}.jpg"))
        feature_path = f"features/{nomeFile}.npy"
        np.save(feature_path, feature)
        