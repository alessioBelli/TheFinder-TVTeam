import math
import cv2
import os
import os.path
from os import path
from utils import query


# take second element for sort
def takeSecond(elem):
    return elem[1]

def istogrammi(input):
    fsRead= cv2.FileStorage ("utils/histograms.yml", cv2.FileStorage_READ )
    
    #calcola istogramma immagine input
    image=cv2.imread(f"images/"+input)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    hists={}
    countc=0
    countr=0
    windowsize_r = math.ceil(image.shape[0]/2)
    windowsize_c = math.ceil(image.shape[1]/2)
 
    for r in range(0,image.shape[0] , windowsize_r):
        for c in range(0,image.shape[1], windowsize_c):
            window = image[r:r+windowsize_r,c:c+windowsize_c]
            hist = cv2.calcHist([window],[0, 1, 2], None,[8, 8, 8],[0, 256, 0, 256, 0, 256]) 
            hists[f'histoquery_{countr}_{countc}'] = cv2.normalize(hist, hist).flatten()
            countc+= 1
        countr+=1
        countc=0

    results={}
    
    image_names = os.listdir("gallery/")
    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]
        compare=0 
        for r in range(0,2):
            for c in range(0,2):
                hist_file=fsRead.getNode(f'histogram_{r}_{c}_{nomeFile}').mat()
                compare+=cv2.compareHist(hists[f'histoquery_{r}_{c}'],hist_file, 0)
                countc+= 1
            countr+=1
            countc=0
        
        media=compare/4
        results[nomeFile]=media


    newdict2={k:v for k, v in sorted(results.items(),reverse=True,key=lambda key:key[1])}
    list_image = os.listdir("./gallery")
    n = len(list_image)
    first_n = list(newdict2.items())[:n]

    return first_n

        
#Funzione che ritorna una stringa json contente le num immagini simili con relativa percentuale a quella di input
def compara(input,num):

    #Comparazione istogrammi tra immagine di input e immagini del dataset
    first_n = istogrammi(input)
    print("Fine comparazione istogrammi")

    #Comparazione tramite feature tra immagine di input e immagini del dataset
    result = query.compara(input)
    print("Fine comparazione tramite feature")

    list_image = os.listdir("./gallery")

    n = len(list_image)
    res = []
    #Creazione vettore contenente il nome delle immagini e la relativa percentuale finale calcolata tramite una media pesata
    for x in range(n):
        for elem in result:
            if elem[0] == first_n[x][0]:
                media = ((first_n[x][1]*100)*0.25 + (elem[1])*0.75) / 1
                res.append((elem[0],media))
            
    #Riordinamento discentente (dal maggiore al minore) del vettore appena creato sulla base del secondo parametro (percentuale)       
    res.sort(key=takeSecond, reverse=True)


    count2=0
    filenames = "["
    #Creazione oggetto json contenente le num immagini simili da visualizzare
    for elem in res:
        count2+=1 
        if(count2 == int(num)):
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": ' + ("%.3f" % (elem[1])) + '}'
            break
        else:
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": ' + ("%.3f" % (elem[1])) + '},'

    filenames = filenames + "]"

    
    return filenames


    
