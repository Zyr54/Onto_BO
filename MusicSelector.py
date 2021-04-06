from owlready2 import *
from random import*
import time
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *

import UI

onto_path = "C:/Users/zyran/OneDrive/Documents/Cours/EMA/Web Semantique/App/Ontologie/BANDEORIGINAL.owl"
onto = get_ontology(onto_path).load()

#print(onto.Attribut)
#print(list(onto.classes()))

#listMusic = onto.

def MusicSelector():
    listResultCat=[]
    listResultUni=[]
    listResultInstru=[]
    if (categorieEntry!="Pas de selection"):
        print("Cat yes")
        catSearch = onto.search_one(iri = "*"+categorieEntry.get())
        print(catSearch)
        listResultCat=[str(x).split(".")[1] for x in onto.search(type = onto.Musique, estDeType=onto.search(is_a = catSearch))]
        print(listResultCat)
    if (universEntry!="Pas de selection"):
        print("Uni yes")
        uniSearch = onto.search_one(iri = "*"+universEntry.get())
        print(uniSearch)
        listResultUni=[str(x).split(".")[1] for x in onto.search(type = onto.Musique, estDeType=onto.search(is_a = uniSearch))]
        print(listResultUni)
    if (instruEntry!="Pas de selection"):
        print("Instru yes")
        instruSearch = onto.search_one(iri = "*"+instruEntry.get())
        print(instruSearch)
        listResultInstru=[str(x).split(".")[1] for x in onto.search(type = onto.Musique, estFaitAvec=onto.search(is_a = instruSearch))]
        print(listResultInstru)

    maxList=0
    listMusic=[]
    listOf=""
    listMusicCounter=[]
    if ( (len(listResultCat) > len(listResultUni) ) and ( len(listResultCat) > len(listResultInstru) ) ):
        maxList=len(listResultCat)
        listOf="Cat"
    elif ( (len(listResultUni) > len(listResultCat) ) and ( len(listResultUni) > len(listResultInstru) ) ):
        maxList=len(listResultUni)
        listOf="Uni"
    else:
        maxList=len(listResultInstru)
        listOf="Instru"

    #print("ListOf: ", listOf)
    #print("maxList: ", maxList)

    if listOf=="Cat":
        for i in range(maxList):
            if ( (listResultCat[i] in listResultUni) and (listResultCat[i] in listResultInstru)):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(3)
            elif ( (listResultCat[i] in listResultUni) or (listResultCat[i] in listResultInstru)):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(2)
            else:
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
    elif listOf=="Uni":
        for i in range(maxList):
            if ( (listResultUni[i] in listResultCat) and (listResultUni[i] in listResultInstru)):
                listMusic.append(listResultUni[i])
                listMusicCounter.append(3)
            elif ( (listResultUni[i] in listResultCat) or (listResultUni[i] in listResultInstru)):
                listMusic.append(listResultUni[i])
                listMusicCounter.append(2)
            else:
                listMusic.append(listResultUni[i])
                listMusicCounter.append(1)
    elif listOf=="Instru":
            for i in range(maxList):
                if ( (listResultInstru[i] in listResultCat) and (listResultInstru[i] in listResultUni)):
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(3)
                elif ( (listResultInstru[i] in listResultCat) or (listResultInstru[i] in listResultUni)):
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(2)
                else:
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(1)

    print(listMusic)
    print(listMusicCounter)

    for i in range(len(listMusic)):
        for k in range(i, len(listMusic)):
            if listMusicCounter[k]>listMusicCounter[i]:
                temp=listMusicCounter[k]
                temp2=listMusic[k]
                listMusicCounter[k]=listMusicCounter[i]
                listMusic[k]=listMusic[i]
                listMusicCounter[i]=temp
                listMusic[i]=temp2

    print("Listes triees par counter decroissant")
    print(listMusic)
    print(listMusicCounter)
    clear_text()
    for x in listMusic:
        insert_text(x)

def test():
    print("OH YEEEEEEAAAAAAAAAAAAAH")
