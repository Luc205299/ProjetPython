# -*- coding: utf-8 -*-
"""Created on Mon Apr 12 13:19:47 2021

@author: Buhard
"""

def Profil() :

#Création du Profil

    Pseudo=str(input("Rentrer votre Speudonyme : "))

    Genre = int(input("Si vous êtes un Homme tapez 1 ; \nSi vous êtes une Femme tapez 2 ; \nSi vous souhaitez ne pas rentrer votre genre, tapez 3 : "))

    match Genre:
        case 1:
            Genre = "Homme"
        case 2 :
            Genre = "Femme"
        case 3 :
            Genre = "Non Précisé"

    # age : en dessous de 18 ans , 18-25 ans  et + de 25 ans
    Age = int(input("Rentrer votre âge : "))
    match Age:
        case Age if Age < 18:
            print("Vous avez en dessous de 18 ans.")
        case Age if Age >= 18 and Age <= 25 :
            print("Vous avez entre 18 et 25 ans.")
        case Age if Age > 25 :
            print("Vous avez au dessus de 25 ans")

    Style = int(input("Rentrer 1 si vous aimer la Science-fiction,\nRentrer 2 si vous aimer la Biographie,\nRentrer 3 si vous aimer l'Horreur,\nRentrer 4 si vous aimer la Romance,\nRentrer 5 si vous aimer les Fables,\nRentrer 6 si vous aimer l'Histoire,\nRentrer 7 si vous aimer la Comédie : "))

def ShowBook(folder:str):
    """function to open and read the Books folder and print what's inside
    folder: the folder un want to read (.txt)"""
    #open folder in read mode
    with open(folder, "r") as f:
        # read open folder
        content = f.readlines()
    cpt=1
    for ligne in content:
        print(cpt,":",str(ligne),'\n')
        cpt+=1
    return()

def addBook(folder:str):
    """function to add a book to the folder at the end
    folder: the folder un want to read (.txt)
    name: the name of the book you want to append"""
    name=str(input("Entrez le titre du livre à ajouter : "))
    exist = False

    #open folder in read mode
    with open(folder, "r") as f:
    # read open folder
        content = f.readlines()
        #print("content :", content , " and ", name ,("?"))
        for ligne in content:
            if content == name:
                print("Ce livre est déjà dans le dépôt")

    if exist == False:
        j = open(folder,"a")
        j.write(name)
    j.close()

def changeTitle(folder:str):
    """function to modify an existing book in folder
    folder: the folder un want to read (.txt)
    name: the name of the book you want to modify"""
    #global addBook()

    name = str(input("Entrez le titre du livre à modifier :"))
    verif=False
    # open folder in read mode
    with open(folder, "r") as f:
        # read open folder
        content = f.readlines()
        for ligne in content:
            print(str(ligne)," et ", name)
            if str(ligne) == name:
                verif=True
                f.write(str(input("Entrez le nouveau nom")))

        if verif==False:
            print("Ce livre n'est pas dans la base donnée")
