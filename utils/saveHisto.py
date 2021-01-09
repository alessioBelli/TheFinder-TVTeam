import cv2
import os
import os.path
from os import path
import math

#Funzione per creare 4 istogrammi per ogni immagine del dataset
def saveHisto():
    
    fsWrite = cv2.FileStorage("utils/histograms.yml", cv2.FileStorage_WRITE )

    #Controllo presenza file non voluto e eliminazione nel caso in cui sia presente
    if path.exists("gallery/.DS_Store"):
        os.remove("gallery/.DS_Store")
    
    image_names = os.listdir("gallery/")

    #Per ogni immagine nel nostro dataset, calcolo dei 4 istogrammi e salvataggio sul file histograms.txt
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

    print("Salvataggio degli istogrammi eseguito correttamente")
    fsWrite.release()

