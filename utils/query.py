
# Import the libraries
import numpy as np
from utils.feature_extractor import FeatureExtractor 
from PIL import Image
import cv2
import os
import tensorflow as tf
import re

#Funzione utilizzata per ordinare i nomi delle immagini presenti nel vettore data (image_names)
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def compara(input):
    fe=FeatureExtractor()
    features=[]
    image_names = sorted_alphanumeric(os.listdir("gallery/"))

    #recupero le feature dai file e le appendo a una lista
    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]
        features.append(np.load(f"features/{nomeFile}.npy"))

    #rendo la lista un Numpy Array    
    features=np.array(features)
    #carico l'immagine di query
    img = Image.open("images/"+input)
    #estraggo le features con il metodo extract della classe esterna FeatureExtractor
    query = fe.extract(img)
    #calcolo la distanza euclidea fra la feature della query e le 1000 salvate
    dists = np.linalg.norm(features - query, axis=1)   #np.linalg.norm formula per distanza eucl
    ids = np.argsort(dists)   #argsort è funzione che ordina in ordine crescente e ritorna gli indici(corrispondenti all'id dell'immagine)

    #creo nuovo array per definire punteggio da 0 a 100
    #-------------------------------------------------------------------
    arr2=np.sort(dists)                    #in arr2 ho i valori ordinati in ordine crescente
    
    oldMax=arr2[len(arr2)-1]              #il vecchio massimo è l'ultimo elemento dell'arr2(che era stato ordinato)    
    if(arr2[0]>0.6):                      #se sono particolarmente simili la distanza sarà a grandi linee inferiore di 0,6
        oldMin=0.6                        #per aumentare i punteggi lavorare su questo(aumentarlo)
    else:
        oldMin=arr2[0]                    #per non avere percentuali che superino il 100% se la distanza minima è minore di 0.6
    newMax=100                            #nuovo punteggio massimo
    newMin=0                              #nuovo minimo

    OldRange = (oldMax-oldMin)            #vecchio range
    NewRange = (newMax-newMin)            #nuovo range
    new=[]
    for n in dists:
        new.append(100-(((n - oldMin) * NewRange) / OldRange) + newMin) #formula per passare da vecchio range a nuovo range(100- per invertire l'ordine (sennò avrei che i più simili sono quelli più vicini allo 0)                                                                  
    #--------------------------------------------------------------------


    result = []
    #Creazione oggetto contente associazione tra nomi e percentuali
    for i in ids:
        nomeFile = os.path.splitext(image_names[i])[0]
        result.append((nomeFile, new[i]))
    return result
