
# Import the libraries
import numpy as np
from feature_extractor import FeatureExtractor 
from PIL import Image
import cv2
import os
import tensorflow as tf
import re


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def compara(input):
    fe=FeatureExtractor()
    features=[]
    image_names = sorted_alphanumeric(os.listdir("gallery/"))
    print(image_names)

    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]
        features.append(np.load(f"features/{nomeFile}.npy"))

    features=np.array(features)

    # Insert the image query
    img = Image.open("images/"+input)
    # Extract its features
    query = fe.extract(img)

    # Calculate the similarity (distance) between images
    dists = np.linalg.norm(features - query, axis=1)     #formula per calcolare la distanza euclidea
    # Extract 10 images that have lowest distance
    ids = np.argsort(dists)[:1000]



    #creo nuovo array per definire punteggio da 0 a 100

    arr2=np.sort(dists)
    oldMax=arr2[len(arr2)-1]    
    if(arr2[0]>0.6):                      #se sono particolarmente simili la distanza sarà a grandi linee inferiore di 0,6
        oldMin=0.6                        #per aumentare i punteggi lavorare su questo(aumentarlo)
    else:
        oldMin=arr2[0]                    #per non avere percentuali che superino il 100% se la distanza minima è minore di 0.6
    newMax=100
    newMin=0

    OldRange = (oldMax-oldMin)
    NewRange = (newMax-newMin)  
    new=[]
    for n in dists:
        new.append(100-(((n - oldMin) * NewRange) / OldRange) + newMin)

    return ids, new