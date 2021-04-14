from owlready2 import *
from random import*
import time
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

#Importation de l'ontologie
owlready2.JAVA_EXE = "C:/Program Files (x86)/Common Files/Oracle/Java/javapath/java.exe"
onto_path = "C:/Users/zyran/OneDrive/Documents/Cours/EMA/Web Semantique/App/Ontologie/BANDEORIGINAL.owl"
onto = get_ontology(onto_path).load()

#Raisonneur mis en commentaire puisqu'il ne fonctionne pas
#with onto:
    #sync_reasoner()


#Fonction effectuant la recherche et affichant le résultat lors de l'appui du bouton rechercher
def MusicSelector():
    listResultCat=[]
    listResultUni=[]
    listResultInstru=[]
    #Pour chaque zone de sélection, si une sélection est faite, alors on va stocké dans une liste toutes les musiques ayant ce critère
    if (categorieEntry.get()!="Pas de selection"):
        catSearch = onto.search_one(iri = "*"+categorieEntry.get())
        listResultCat=onto.search(type = onto.Musique, estDeType=onto.search(is_a = catSearch))
    if (universEntry.get()!="Pas de selection"):
        uniSearch = onto.search_one(iri = "*"+universEntry.get())
        listResultUni=onto.search(type = onto.Musique, provientDe=onto.search(is_a = onto.Oeuvre, estDansUnivers=onto.search(is_a = uniSearch)))
    if (instruEntry.get()!="Pas de selection"):
        instruSearch = onto.search_one(iri = "*"+instruEntry.get())
        listResultInstru=onto.search(type = onto.Musique, estFaitAvec=onto.search(is_a = instruSearch))

    listMusic=[]
    listMusicCounter=[]
    listAuthor=[]
    testPopular=populariteBool.get()
    testTheme=themeBool.get()

    #On parcours toutes les musiques dans la liste liée à la sélection "Catégorie"
    for i in range(len(listResultCat)):
        # /!\ La clause if suivante n'aurait pas dû être implémentée en python si le Raisonneur avait fonctionné
        #Si on veut des thèmes ET des musiques populaires seulement, alors on va vérifié que la i-ème musique de la liste possède ces 2 critères,
        #Si c'est le cas, alors on l'ajoute dans la liste des musiques finales et on dit qu'elle a été trouvé dans une lise (cele-ci)
        if(testPopular and testTheme):
            if(listResultCat[i].VueYoutube>=5 and listResultCat[i].isTheme==True):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        #Sinon, si on veut des musiques populaire SEULEMENT, alors on vérifie que la i-ème musique l'est, si c'est le cas, alors on
        #l'ajoute comme pour la clause précédente
        elif(testPopular):
            if(listResultCat[i].VueYoutube>=5):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        #Idem que pour la popularité seulement mais pour le thème seulement
        elif(testTheme):
            if(listResultCat[i].isTheme==True):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        #Et dans tout les autres cas, on ajoute la i-ème musique avec une valeur associée de 1
        else:
            listMusic.append(listResultCat[i])
            listMusicCounter.append(1)

    #Même principe que pour la liste des musique de la sélection catégorie, mais pour la liste de la sélection Univers
    for i in range(len(listResultUni)):
        if(testPopular and testTheme):
            if(listResultUni[i].VueYoutube>=5 and listResultUni[i].isTheme==True):
                #Test de si la musique appartient deja à la liste des musique.
                #Si c'est le cas, alors on va récupérer à quel index est la musique, et on va incrémenter son compteur de 1 pour dire
                #qu'on la trouvé dans une autre liste
                if(listResultUni[i] in listMusic):
                    tracker=listMusic.index(listResultUni[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultUni[i])
                    listMusicCounter.append(1)
        elif(testPopular):
            if(listResultUni[i].VueYoutube>=5):
                if(listResultUni[i] in listMusic):
                    tracker=listMusic.index(listResultUni[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultUni[i])
                    listMusicCounter.append(1)
        elif(testTheme):
            if(listResultUni[i].isTheme==True):
                if(listResultUni[i] in listMusic):
                    tracker=listMusic.index(listResultUni[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultUni[i])
                    listMusicCounter.append(1)
        else:
            if(listResultUni[i] in listMusic):
                tracker=listMusic.index(listResultUni[i])
                listMusicCounter[tracker]+=1
            else:
                listMusic.append(listResultUni[i])
                listMusicCounter.append(1)

    #Exactement le même principe que pour la liste de la sélection d'univers
    for i in range(len(listResultInstru)):
        if(testPopular and testTheme):
            if(listResultInstru[i].VueYoutube>=5 and listResultInstru[i].isTheme==True):
                if(listResultInstru[i] in listMusic):
                    tracker=listMusic.index(listResultInstru[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(1)
        elif(testPopular):
            if(listResultInstru[i].VueYoutube>=5):
                if(listResultInstru[i] in listMusic):
                    tracker=listMusic.index(listResultInstru[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(1)
        elif(testTheme):
            if(listResultInstru[i].isTheme==True):
                if(listResultInstru[i] in listMusic):
                    tracker=listMusic.index(listResultInstru[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(1)
        else:
            if(listResultInstru[i] in listMusic):
                tracker=listMusic.index(listResultInstru[i])
                listMusicCounter[tracker]+=1
            else:
                listMusic.append(listResultInstru[i])
                listMusicCounter.append(1)

    #On va trier la liste des musique par rapport à leurs pertinence par rapport aux critères de recherches
    #On procède donc avec un tri par insertion
    for i in range(len(listMusic)):
        for k in range(i, len(listMusic)):
            if listMusicCounter[k]>listMusicCounter[i]:
                temp=listMusicCounter[k]
                temp2=listMusic[k]
                listMusicCounter[k]=listMusicCounter[i]
                listMusic[k]=listMusic[i]
                listMusicCounter[i]=temp
                listMusic[i]=temp2


    clear_text()
    count=0
    musicsInPlaylist=0
    #On vérifie qu'un temps de playlist max n'est pas précisé, si y'a à un, alors on va compté combien de musiques de la liste on peut afficher
    #On utilise donc un compteur qui servira plus tard
    if(tempsPlaylistVar.get()!=''):
        tempsMax=tempsPlaylistVar.get()
        minuteCumulee=0
        secondeCumulee=0
        for x in listMusic:
            DureeMusique=str(x.Duree)
            MinuteMusique=re.sub(r"\[","",str(DureeMusique).split(".")[0])
            SecondeMusique=re.sub(r"\]","",str(DureeMusique).split(".")[1])
            minuteCumulee+=int(MinuteMusique)
            secondeCumulee+=int(SecondeMusique)
            if(secondeCumulee>=60):
                secondeCumulee-=60
                minuteCumulee+=1
            musicsInPlaylist+=1
            if(minuteCumulee>int(tempsMax)):
                break


    rate=0
    #On compte combien de critères ont été utilisés
    if(categorieEntry.get()!="Pas de selection"):
        rate+=1
    if(universEntry.get()!="Pas de selection"):
        rate+=1
    if(instruEntry.get()!="Pas de selection"):
        rate+=1

    #On affiche dans la zone d'affichage, dans l'ordre: Le taux de pertinence, le titre de la musique, le nom de l'oeuvre, le temps de la musique
    for x in listMusic:
        count+=1
        at=listMusic.index(x)
        foundRate=round(listMusicCounter[at]/rate, 2)
        DureeMusique=str(x.Duree)
        DureeMusique=re.sub(r"\.",":",DureeMusique)
        Oeuvre=onto.search_one(type = onto.Oeuvre, ContientMusique=onto.search(is_a = x))
        textAAfficher="("+str(foundRate)+") "+str(x.label)+" - "+str(Oeuvre.label)+" ("+DureeMusique+")"
        textAAfficher=re.sub(r"\[|\]|'|\"","",textAAfficher)
        print(textAAfficher)
        insert_text(textAAfficher)
        #On vérifie qu'on ne dépasse pas le nombre de musique max demandée ET le temps de la playlist (donc le nombre de musique max calculé au préalable),
        #Ou l'un des deux
        if(nbrMusiqueVar.get()!='') and (tempsPlaylistVar.get()!=''):
            if(count>=int(nbrMusiqueVar.get())) or (count>=musicsInPlaylist):
                break
        elif(nbrMusiqueVar.get()!='') or (tempsPlaylistVar.get()!=''):
            if(tempsPlaylistVar.get()!=''):
                if(count>=musicsInPlaylist):
                    break
            elif(nbrMusiqueVar.get()!=''):
                if(count>=int(nbrMusiqueVar.get())):
                    break


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



#Fonction d'affichage de texte
def insert_text(text):
    resultArea.config(state=NORMAL)
    resultArea.insert(INSERT,f"{text}\n")
    #resultArea.see(END)
    resultArea.config(state=DISABLED)
    resultArea.update()

#Fonction pour delete le texte
def clear_text():
    resultArea.config(state=NORMAL)
    resultArea.delete('1.0', END)
    resultArea.config(state=DISABLED)
    resultArea.update()

searchButton=Button(can,text="Rechercher",font="Calibri 16",overrelief ="ridge",command=MusicSelector)
searchButton.grid(row=7, column=1, columnspan=2)

#Display résultat
scrollbar = Scrollbar(can)
resultArea=Text(can, height=10, width=50, font="Calibri 16 bold", bd=4, relief=RIDGE, bg='#BBBBBB', state=DISABLED, yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=4, rowspan=7, padx=0, pady=0, sticky=N+S)
scrollbar.config(command=resultArea.yview)
resultArea.grid(row=1, column=3, rowspan=7, padx=20, pady=20)


appScreen.mainloop()
