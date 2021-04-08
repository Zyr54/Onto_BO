from owlready2 import *
from random import*
import time
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
import re

owlready2.JAVA_EXE = "C:/Program Files (x86)/Common Files/Oracle/Java/javapath/java.exe"
onto_path = "C:/Users/zyran/OneDrive/Documents/Cours/EMA/Web Semantique/App/Ontologie/BANDEORIGINAL.owl"
onto = get_ontology(onto_path).load()

#with onto:
    #sync_reasoner()



def MusicSelector():
    listResultCat=[]
    listResultUni=[]
    listResultInstru=[]
    #str(x).split(".")[1] for x in
    if (categorieEntry.get()!="Pas de selection"):
        #print("Cat yes")
        catSearch = onto.search_one(iri = "*"+categorieEntry.get())
        #print(catSearch)
        listResultCat=onto.search(type = onto.Musique, estDeType=onto.search(is_a = catSearch))
        #print(listResultCat)
    if (universEntry.get()!="Pas de selection"):
        #print("Uni yes")
        uniSearch = onto.search_one(iri = "*"+universEntry.get())
        #print(uniSearch)
        listResultUni=onto.search(type = onto.Musique, provientDe=onto.search(is_a = onto.Oeuvre, estDansUnivers=onto.search(is_a = uniSearch)))
        #print(listResultUni)
    if (instruEntry.get()!="Pas de selection"):
        #print("Instru yes")
        instruSearch = onto.search_one(iri = "*"+instruEntry.get())
        #print(instruSearch)
        listResultInstru=onto.search(type = onto.Musique, estFaitAvec=onto.search(is_a = instruSearch))
        #print(listResultInstru)

    listMusic=[]
    listMusicCounter=[]
    listAuthor=[]
    testPopular=populariteBool.get()
    testTheme=themeBool.get()

    #print("TESTPOP=",testPopular)
    for i in range(len(listResultCat)):
        if(testPopular and testTheme):
            if(listResultCat[i].VueYoutube>=5 and listResultCat[i].isTheme==True):
                #print("Both Pop and Theme: ",listResultCat[i])
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        elif(testPopular):
            #print("CAT: ",listResultCat[i]," vue=",listResultCat[i].VueYoutube)
            if(listResultCat[i].VueYoutube>=5):
                #print("CAT: Test ok for: ",listResultCat[i])
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        elif(testTheme):
            if(listResultCat[i].isTheme==True):
                listMusic.append(listResultCat[i])
                listMusicCounter.append(1)
        else:
            #print("CAT: Else pour: ", listResultCat[i])
            listMusic.append(listResultCat[i])
            listMusicCounter.append(1)
        #print("CAT:",listMusic)
    for i in range(len(listResultUni)):
        if(testPopular and testTheme):
            if(listResultUni[i].VueYoutube>=5 and listResultUni[i].isTheme==True):
                #print("Both Pop and Theme: ",listResultUni[i])
                if(listResultUni[i] in listMusic):
                    tracker=listMusic.index(listResultUni[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultUni[i])
                    listMusicCounter.append(1)
        elif(testPopular):
            #print("UNI: ",listResultUni[i]," vue=",listResultUni[i].VueYoutube)
            if(listResultUni[i].VueYoutube>=5):
                #print("UNI: Test ok for: ",listResultUni[i])
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
            #print("UNI: Else pour: ", listResultUni[i])
            if(listResultUni[i] in listMusic):
                tracker=listMusic.index(listResultUni[i])
                listMusicCounter[tracker]+=1
            else:
                listMusic.append(listResultUni[i])
                listMusicCounter.append(1)
        #print("UNI:",listMusic)
    for i in range(len(listResultInstru)):
        if(testPopular and testTheme):
            if(listResultInstru[i].VueYoutube>=5 and listResultInstru[i].isTheme==True):
                #print("Both Pop and Theme: ",listResultInstru[i])
                if(listResultInstru[i] in listMusic):
                    tracker=listMusic.index(listResultInstru[i])
                    listMusicCounter[tracker]+=1
                else:
                    listMusic.append(listResultInstru[i])
                    listMusicCounter.append(1)
        elif(testPopular):
            #print("INSTRU: ",listResultInstru[i]," vue=",listResultInstru[i].VueYoutube)
            if(listResultInstru[i].VueYoutube>=5):
                #print("INSTRU: Test ok for: ",listResultInstru[i])
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
            #print("INSTRU: Else pour: ", listResultInstru[i])
            if(listResultInstru[i] in listMusic):
                tracker=listMusic.index(listResultInstru[i])
                listMusicCounter[tracker]+=1
            else:
                listMusic.append(listResultInstru[i])
                listMusicCounter.append(1)
        #print("INSTRU:",listMusic)

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
    count=0
    musicsInPlaylist=0
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
            #print(minuteCumulee,":",secondeCumulee)
            #print("Minute de la musique: "+MinuteMusique)
            #print("Seconde de la musique: "+SecondeMusique)


    rate=0
    if(categorieEntry.get()!="Pas de selection"):
        rate+=1
    if(universEntry.get()!="Pas de selection"):
        rate+=1
    if(instruEntry.get()!="Pas de selection"):
        rate+=1

    for x in listMusic:
        #print("Is",x,"a theme? ",x.isTheme)
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



#Gestion bouton recherche
def insert_text(text):
    resultArea.config(state=NORMAL)
    resultArea.insert(INSERT,f"{text}\n")
    #resultArea.see(END)
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



searchButton=Button(can,text="Rechercher",font="Calibri 16",overrelief ="ridge",command=MusicSelector)
searchButton.grid(row=7, column=1, columnspan=2)

#Display résultat
scrollbar = Scrollbar(can)
resultArea=Text(can, height=10, width=50, font="Calibri 16 bold", bd=4, relief=RIDGE, bg='#BBBBBB', state=DISABLED, yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=4, rowspan=7, padx=0, pady=0, sticky=N+S)
scrollbar.config(command=resultArea.yview)
resultArea.grid(row=1, column=3, rowspan=7, padx=20, pady=20)


appScreen.mainloop()
