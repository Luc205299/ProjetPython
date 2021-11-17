"""Created on Mon Apr 12 13:19:47 2021

@author: Buhard
"""
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
    with open(folder, "r", encoding='utf-8') as f:
    # read open folder
        content = f.readlines()
        for ligne in content:
            ligne2 = ligne.strip('\n')
            #print("ligne2 :", ligne, " and ", name, ("?"))
            if ligne2 == name:
                print("Ce livre est déjà dans le dépôt")
                exist=True

    if exist == False:
        j = open(folder,"a", encoding='utf-8')
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
