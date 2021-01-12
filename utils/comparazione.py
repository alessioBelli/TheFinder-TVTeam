import math
import cv2
import os
import os.path
from os import path
import numpy as np
from utils import query


# take second element for sort
def takeSecond(elem):
    return elem[1]

def istogrammi(input):
    fsRead= cv2.FileStorage ("utils/histograms.yml", cv2.FileStorage_READ )			#legge e salva i risultati nel file specificato
    
    #calcola istogramma immagine input
    image=cv2.imread(f"images/"+input)												#prende in input l'immagine
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)									#effettua la conversione dei colori 
    
    hists={}
    countc=0
    countr=0
    windowsize_r = math.ceil(image.shape[0]/2)										 #crea una finestra per le righe di dimensione pari a metà della larghezza dell'immagine e la approssima all'intero più vicino
    windowsize_c = math.ceil(image.shape[1]/2) 										#crea una finestra per le colonne di dimensione pari a metà dell'altezza dell'immagine e la approssima all'intero più vicino
 
    for r in range(0,image.shape[0] , windowsize_r):											#cicla per spostare la finestra lungo tutta la larghezza dell'immagine
        for c in range(0,image.shape[1], windowsize_c):											#cicla per spostare la finestra lungo tutta l'altezza dell'immagine
            window = image[r:r+windowsize_r,c:c+windowsize_c]									#definizione della finestra 
            hist = cv2.calcHist([window],[0, 1, 2], None,[8, 8, 8],[0, 256, 0, 256, 0, 256]) 	#calcola l'istogramma associato alla finstra
            hists[f'histoquery_{countr}_{countc}'] = cv2.normalize(hist, hist).flatten()		#normalizza l'istogramma
            countc+= 1
        countr+=1
        countc=0

    results={}
    
    image_names = os.listdir("gallery/")														#salva i nomi delle immagini
    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]												#separa il percorso per l'immagine cioè divide il nome della radice dal nome dell'immagine
        compare=0 
        for r in range(0,2):
            for c in range(0,2):
                hist_file=fsRead.getNode(f'histogram_{r}_{c}_{nomeFile}').mat()					#legge il file contenente i dati sugli istogrammi 
                compare+=cv2.compareHist(hists[f'histoquery_{r}_{c}'],hist_file, 0)				#compara le relative regioni di ogni immagine
                countc+= 1
            countr+=1
            countc=0
        
        media=compare/4																			#calcola la media  
        results[nomeFile]=media																	#salva la media relativa 

    #ids = np.argsort(results)   #argsort è funzione che ordina in ordine crescente e ritorna gli indici(corrispondenti all'id dell'immagine)
    d=list(results.values())
    
    #creo nuovo array per definire punteggio da 0 a 100
    #-------------------------------------------------------------------
    ids=np.argsort(d)
    arr2=np.sort(d)                    #in arr2 ho i valori ordinati in ordine crescente

    oldMax=arr2[len(arr2)-1]              
    oldMin=arr2[0]                    
    newMax=arr2[len(arr2)-1]                            #nuovo punteggio massimo
    newMin=0                              #nuovo minimo

    OldRange = (oldMax-oldMin)            #vecchio range
    NewRange = (newMax-newMin)            #nuovo range
    new=[]
    for n in d:
        new.append((((n - oldMin) * NewRange) / OldRange) + newMin) #formula per passare da vecchio range a nuovo range(100- per invertire l'ordine (sennò avrei che i più simili sono quelli più vicini allo 0)                                                                  
    #--------------------------------------------------------------------
    
    result_histograms = []
    #Creazione oggetto contente associazione tra nomi e percentuali
    for i in ids:
        nomeFile = os.path.splitext(image_names[i])[0]
        result_histograms.append((nomeFile, new[i]))

    return result_histograms

        
#Funzione che ritorna una stringa json contente le num immagini simili con relativa percentuale a quella di input
def compara(input,num):

    #Comparazione istogrammi tra immagine di input e immagini del dataset
    result_histograms = istogrammi(input)
    print("Fine comparazione istogrammi")
    #Comparazione tramite feature tra immagine di input e immagini del dataset
    result_features = query.compara(input)
    print("Fine comparazione tramite feature")

    list_image = os.listdir("./gallery")

    n = len(list_image)
    res = []
    #Creazione vettore contenente il nome delle immagini e la relativa percentuale finale calcolata tramite una media pesata
    for x in range(n):
        for elem in result_features:
            if elem[0] == result_histograms[x][0]:	                                                        #se nome file del risultato feature è uguale a nome file risultato istogramma
                
                media = ((result_histograms[x][1])*0.25*100 + (elem[1])*0.75) / 1								# 25% peso istogrammi  75% features
                res.append((elem[0],media, result_histograms[x][1]*100, elem[1] ))
            
    #Riordinamento discentente (dal maggiore al minore) del vettore appena creato sulla base del secondo parametro (percentuale)       
    res.sort(key=takeSecond, reverse=True)


    count2=0
    filenames = "["
    #Creazione oggetto json contenente le num immagini simili da visualizzare
    for elem in res:
        count2+=1 
        if(count2 == int(num)):
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": "' + ("%.3f" % (elem[1])) + '", "percentage_histo": "' + ("%.3f" % (elem[2])) + '", "percentage_features": "' + ("%.3f" % (elem[3])) + '"}'
            break
        else:
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": "' + ("%.3f" % (elem[1])) + '", "percentage_histo": "' + ("%.3f" % (elem[2])) + '", "percentage_features": "' + ("%.3f" % (elem[3])) + '"},'

    filenames = filenames + "]"

    return filenames


    
