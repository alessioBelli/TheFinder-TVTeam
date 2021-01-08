from feature_extractor import FeatureExtractor
from pathlib import Path
from PIL import Image
import numpy as np
import os
import sys

#Funzione per la creazione delle feature per ogni immagine del dataset
def creazioneFeature():
    fe = FeatureExtractor()
    #Controllo presenza cartella ./featurem, creazione se non ci dovesse essere
    if os.path.isdir("./features") == True:
        print("Directory già presente")
    else:
        os.mkdir("./features")

    image_names = os.listdir("gallery/")

    cont = 0
    #Estrazione feature per ogni immagine e salvataggio nella cartella ./feature
    for filename in image_names:
        cont = cont+1

        #Visualizzazione numero immagini eleborate nella console
        if cont % 10 == 0:
            sys.stdout.write('\r' + "Le immagini elaborate sono attualmente : " + str(cont) + "/" + str(len(image_names)))
            sys.stdout.flush() 
        if cont == len(image_names):
            sys.stdout.write('\r' + "Le immagini elaborate sono attualmente : " + str(cont) + "/" + str(len(image_names)))
            sys.stdout.flush() 
            
        nomeFile = os.path.splitext(filename)[0]
        feature = fe.extract(img=Image.open(f"gallery/{nomeFile}.jpg"))
        feature_path = f"features/{nomeFile}.npy"
        np.save(feature_path, feature)



if __name__ == "__main__":
    creazioneFeature()