import time
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from owlready2 import *

onto_path = "C:/Users/zyran/OneDrive/Documents/Cours/EMA/Web Semantique/App/Ontologie/BANDEORIGINAL.owl"
onto = get_ontology(onto_path).load()

#print(onto.Attribut)
#print(list(onto.classes()))

#listMusic = onto.

appScreen=Tk()
appScreen.title("Music Selector")
appScreen.resizable(height=False,width=False)

h=450
w=900

can=Canvas(appScreen, height=h, width=w)
can.grid(row=1,column=1)

#Gestion affichage Catégorie
categorieLabel=Label(can,text="Catégorie", font="Calibri 16 bold")
categorieLabel.grid(row=1,column=1)
listCat=["Pas de selection"]+[str(x).split(".")[1] for x in onto.search(type = onto.Categorie)]
categorieEntry=ttk.Combobox(can, values=listCat, font="Calibri 16", state="readonly")
categorieEntry.grid(row=2,column=1)
categorieEntry.current(0);

#Gestion Affichage Univers
universLabel=Label(can,text="Univers", font="Calibri 16 bold")
universLabel.grid(row=3,column=1)
listUni=["Pas de selection"]+[str(x).split(".")[1] for x in onto.search(type = onto.Univers)]
universEntry=ttk.Combobox(can, values=listUni, font="Calibri 16", state="readonly")
universEntry.grid(row=4,column=1)
universEntry.current(0);

#Gestion Affichage Type Instrument
instruLabel=Label(can,text="Type d'instrumental", font="Calibri 16 bold")
instruLabel.grid(row=5,column=1)
listIntru=["Pas de selection"]+[str(x).split(".")[1] for x in onto.search(type = onto.Instrument)]
instruEntry=ttk.Combobox(can, values=listIntru, font="Calibri 16", state="readonly")
instruEntry.grid(row=6,column=1)
instruEntry.current(0);

#Gestion affichage nombre musique
nbrMusiqueLabel=Label(can,text="# musiques", font="Calibri 16 bold")
nbrMusiqueLabel.grid(row=1, column=2)
nbrMusiqueVar=StringVar()
nbrMusiqueEntry=Entry(can, textvariable=nbrMusiqueVar, font="Calibri 16")
nbrMusiqueEntry.grid(row=2, column=2,padx=20)

#Gestion Affichage Temps Playlist
tempsPlaylistLabel=Label(can,text="Temps Playlist (en min)", font="Calibri 16 bold")
tempsPlaylistLabel.grid(row=3, column=2)
tempsPlaylistVar=StringVar()
tempsPlaylistEntry=Entry(can, textvariable=tempsPlaylistVar, font="Calibri 16")
tempsPlaylistEntry.grid(row=4, column=2,padx=20)

#Gestion Affichage Popularité
populariteBool=IntVar()
populariteCB=Checkbutton(can, text="Populaire only?", variable=populariteBool, onvalue=1, offvalue=0, font="Calibri 16 bold")
populariteCB.grid(row=5, column=2)

#Gestion affichage Theme
themeBool=IntVar()
themeCB=Checkbutton(can, text="Theme only?", variable=themeBool, onvalue=1, offvalue=0, font="Calibri 16 bold")
themeCB.grid(row=6, column=2)

#Gestion bouton recherche
def insert_text(text):
    resultArea.config(state=NORMAL)
    resultArea.insert(INSERT,f"{text}\n")
    resultArea.see(END)
    resultArea.config(state=DISABLED)
    resultArea.update()

def clear_text():
    resultArea.config(state=NORMAL)
    resultArea.delete('1.0', END)
    resultArea.config(state=DISABLED)
    resultArea.update()

i = 0
def noCommandyet():
    global i
    resultArea.config(state=NORMAL)
    resultArea.insert(INSERT,f"Bouton recherche appuye {i}\n")
    i += 1
    resultArea.see(END)
    resultArea.config(state=DISABLED)
    resultArea.update()


searchButton=Button(can,text="Rechercher",font="Calibri 16",overrelief ="ridge",command=MusicSelector.MusicSelector())
searchButton.grid(row=7, column=1, columnspan=2)

#Display résultat
resultArea=Text(can, height=10, width=40, font="Calibri 16 bold", bd=4, relief=RIDGE, bg='#BBBBBB', state=DISABLED)
resultArea.grid(row=1, column=3, rowspan=7, padx=20, pady=20)

appScreen.mainloop()
