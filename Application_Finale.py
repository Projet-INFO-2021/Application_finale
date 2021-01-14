from tkinter import*
from tkinter import filedialog
import os
import ftp
import CSV
import shutil
import sys
from os.path import basename


#creation de la fenetre et ses paramètres
fenetre = Tk()
fenetre.title('publication')
fenetre.geometry('780x500')
fenetre.configure(bg='white') 
fenetre.resizable(width=NO,height=NO)
chemin1 = ''
chemin2 = ''
chemin3 = ''
chemin4 = ''
chemin1F = ''
chemin2F = ''
chemin3F = ''
chemin4F = ''
testeur = 0

#recupère un fichier 
def openfile1():
    global chemin1
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin1 = os.path.abspath(rep_file)
    ouvrir1 = Button(fenetre, text="OK", command=openfile1,bg='#3e484f',font=('Courier','11'),cursor='bottom_side',foreground='white',width=7)
    ouvrir1.grid(column=0,row=6)
    return chemin1

#recupère un fichier
def openfile2():
    global chemin2
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin2 = os.path.abspath(rep_file)
    ouvrir2 = Button(fenetre, text="OK", command=openfile2,bg='#3e484f',font=('Courier','11'),cursor='bottom_side',foreground='white',width=7)
    ouvrir2.grid(column=1,row=6)
    return chemin2

#recupère un fichier
def openfile3():
    global chemin3
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin3 = os.path.abspath(rep_file)
    ouvrir3 = Button(fenetre, text="OK", command=openfile3,bg='#3e484f',font=('Courier','11'),cursor='bottom_side',foreground='white',width=7)
    ouvrir3.grid(column=2,row=6)
    return chemin3

#recupère un dossier 
def openfile4():
    global chemin4
    chemin4 = filedialog.askdirectory()
    ouvrir4 = Button(fenetre, text="OK", command=openfile4,bg='#3e484f',font=('Courier','11'),cursor='bottom_side',foreground='white',width=7)
    ouvrir4.grid(column=3,row=6)
    return chemin4

def boutonvalider():
    global module
    module=saisie.get()
    fenetre.destroy()
    

bienvenue=Label(fenetre,text='BIENVENUE DANS VOTRE ESPACE DE PUBLICATION',background='#6be1e3',relief='flat',foreground='white',height=5,width=65,font=('Candara Light', 15,'bold'))
bienvenue.grid(column=0,row=0,rowspan=2,columnspan=4)
explication=Label(fenetre, text='Veuillez sélectionner vos 3 fichiers CSV et votre dossier principal',height=5,width=50,font=('Candara Light',13,'underline'),bg='white')
explication.grid(column=0,row=3,rowspan=2,columnspan=4)

explication1=Label(fenetre, text='CSV Module',font=('Verdana','10'),bg='white')
explication1.grid(column=0,row=5,pady=4)
ouvrir1 = Button(fenetre, text="Ouvrir", command=openfile1,bg='#ccd8df',font=('Courier','11'),cursor='bottom_side')
ouvrir1.grid(column=0,row=6)

explication2=Label(fenetre, text='CSV Structure',font=('Verdana','10'),bg='white')
explication2.grid(column=1,row=5)
ouvrir2 = Button(fenetre, text="Ouvrir", command=openfile2,bg='#ccd8df',font=('Courier','11'),cursor='bottom_side')
ouvrir2.grid(column=1,row=6)

explication3=Label(fenetre, text='CSV Description',font=('Verdana','10'),bg='white')
explication3.grid(column=2,row=5)
ouvrir3 = Button(fenetre, text="Ouvrir", command=openfile3,bg='#ccd8df',font=('Courier','11'),cursor='bottom_side')
ouvrir3.grid(column=2,row=6)

explication4=Label(fenetre, text='Dossier principal',bg='white',font=('Verdana','10'))
explication4.grid(column=3,row=5)
ouvrir4 = Button(fenetre, text="Ouvrir", command=openfile4,bg='#ccd8df',font=('Courier','11'),cursor='bottom_side')
ouvrir4.grid(column=3,row=6)


blanc=Label(fenetre, text='           ',bg='white',height=3)
blanc.grid(column=1,row=7)

explication5=Label(fenetre, text='               Incrivez le nom du module que vous voulez :',bg='white',font=('Candara Light',13))
explication5.grid(column=0,row=8,columnspan=2)

saisie=Entry(fenetre,bg='white',width=20,cursor='xterm')
saisie.grid(column=2,row=8)

blanc1=Label(fenetre, text='           ',bg='white',height=3)
blanc1.grid(column=1,row=9)

fermer = Button(fenetre, text="Valider", command=boutonvalider,activebackground='black',bd=6,bg='#3e484f',height=2,width=13,font=('Courier','13'),cursor='hand1',relief=RIDGE,takefocus='shift-tab',foreground='white')
fermer.grid(column=1,row=10, columnspan=2,rowspan=2)


fenetre.mainloop()


while testeur == 0:
    if chemin1 != '':
        chemin1F = chemin1
        chemin1 = ''
    if chemin2 != '':
        chemin2F = chemin2
        chemin2 = ''
    if chemin3 != '':
        chemin3F = chemin3
        chemin3 = ''
    if chemin4 != '':
        chemin4F = chemin4
        chemin4 = ''
    if chemin1F != '' and chemin2F != '' and chemin3F != '' and chemin4F != '':
        testeur = 1

print('Chemin1', chemin1F)
print('Chemin2', chemin2F)
print('Chemin3', chemin3F)
print('Chemin4', chemin4F)
print('Module',module)




nom1 = basename(chemin1F)
nom2 = basename(chemin2F)
nom3 = basename(chemin3F)
nom4 = basename(chemin4F)

print(nom1)
print(nom2)
print(nom3)
print(nom4)
 

Chemin1 = r'C:\Users\jroua\Desktop\Test\Module_csv.csv'
Chemin2 = r'C:\Users\jroua\Desktop\Test\Structure_csv.csv'
Chemin3 = r'C:\Users\jroua\Desktop\Test\Description_csv.csv'
Chemin4 = r'C:/Users/jroua/Desktop/Test/Ressources'
nom_du_module = module


CSV.CSV(chemin1F, chemin2F, chemin3F, chemin4F, nom_du_module)

print(os.getcwd())

Fichier = os.getcwd() + '\\' + nom_du_module 

ftp.uploaddossier(Fichier, nom_du_module)
