import cv2
from matplotlib import pyplot as plt
# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
import os
import os.path
from os import path
import query


# take second element for sort
def takeSecond(elem):
    return elem[1]

def compara(input):
    fsRead= cv2.FileStorage ("histograms.txt", cv2.FileStorage_READ )


    #calcola istogramma immagine input
    image=cv2.imread(f"images/"+input)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist([image],[0, 1, 2], None,[8, 8, 8],[0, 256, 0, 256, 0, 256]) 
    hist = cv2.normalize(hist, hist).flatten()

    results={}

    image_names = os.listdir("gallery/")
    for filename in image_names:
        nomeFile = os.path.splitext(filename)[0]
        hist_file=fsRead.getNode(f'histogram_{nomeFile}').mat()
        compare=cv2.compareHist(hist,hist_file, 0)
        results[nomeFile]=compare


    newdict2={k:v for k, v in sorted(results.items(),reverse=True,key=lambda key:key[1])}
    n=1000
    first_n = list(newdict2.items())[:n]
    print (first_n)

    ids,new = query.compara(input)
    
    res = []
    for x in range(n):
        #print(first_n[x][0])
        for i in ids:
            if str(i) == first_n[x][0]:
                #print("Img:", i)
                #print("Hist:",first_n[x][1])
                #print("Deep:",new[i])
                media = ((first_n[x][1]*100)*0.2 + (new[i])*0.8) / 1
                res.append((i,media))
    print(res)
    
    res.sort(key=takeSecond, reverse=True)
    print("Sorted",res)

    count2=0
    filenames = "["
    for elem in res:
        count2+=1 
        if(count2 == 6):
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": ' + ("%.3f" % (elem[1])) + '}'
            break
        else:
            filenames = filenames + '{ "name": "' + f"{elem[0]}.jpg" + '", "percentage": ' + ("%.3f" % (elem[1])) + '},'

    filenames = filenames + "]"

    '''
    # loop over the results
    count2=0
    filenames = "["
    for (i,k) in first_n:
        count2+=1 
        if(count2 == n):
            filenames = filenames + '{ "name": "' + f"{i}.jpg" + '", "percentage": ' + ("%.3f" % (k)) + '}'
        else:
            filenames = filenames + '{ "name": "' + f"{i}.jpg" + '", "percentage": ' + ("%.3f" % (k)) + '},'

    filenames = filenames + "]"
    '''
    #filenames = '[{ "name": "0.jpg", "percentage": 43},{ "name": "1.jpg", "percentage": 12},{ "name": "2.jpg", "percentage": 90},{ "name": "134.jpg", "percentage": 56},{ "name": "4.jpg", "percentage": 34}]'
    return filenames

        
