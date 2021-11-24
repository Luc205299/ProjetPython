"""Created on Mon Apr 12 13:19:47 2021

@author: Buhard
"""
def ShowBook(file:str):
    """function to open and read the Books file and print what's inside
    file: the file un want to read (.txt)"""
    #open file in read mode
    with open(file, "r") as f:
        # read open file
        content = f.readlines()
    cpt=1
    for ligne in content:
        print(cpt,":",str(ligne),'\n')
        cpt+=1
    return()

def addBook(file:str):
    """function to add a book at the end of the file
    file: the file un want to read (.txt)
    name: the name of the book you want to append"""
    name=str(input("Entrez le titre du livre à ajouter : "))
    exist = False
    #open file in read mode
    with open(file, "r", encoding='utf-8') as f:
    # read open file
        content = f.readlines()
        for ligne in content:
            ligne2 = ligne.strip('\n')
            #print("ligne2 :", ligne, " and ", name, ("?"))
            if ligne2 == name:
                print("Ce livre est déjà dans le dépôt")
                exist=True

    if exist == False:
        j = open(file,"a", encoding='utf-8')
        j.write(name)
        j.close()

def changeTitle(file:str):
    """function to modify an existing book in file
    file: the file un want to read (.txt)
    name: the name of the book you want to modify"""

    name = str(input("Entrez le titre du livre à modifier :"))
    index_src = None
    #list of file data
    data_list=[]
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            #print(ligne," et ", name)
            data_list.append(ligne)
            if str(ligne) == name:

                index_src = content.index(ligne)
                #print(index_src, "index src")

    if index_src == None :
        return(print("Ce livre n'est pas dans la base donnée"))

    elif type(index_src) == int:
        #print("verif ", data_list[index_src])
        #2nd open of the file to modify data
        new_title = str(input("Quel est le nouveau titre de ce livre?"))
        data_list[index_src] = new_title
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt)


def delete_Book(file:str):
    """ delete an existing book from the repository/library of file in argument
    file: str the file in question """

    name = str(input("Entrez le titre du livre à suuprimmer :"))
    index_src = None
    #list of file data
    data_list=[]
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            #print(ligne," et ", name)
            data_list.append(ligne)
            if str(ligne) == name:

                index_src = content.index(ligne)
                print(index_src, "index src")

    if index_src == None :
        return(print("Ce livre n'est pas dans la base donnée"))

    elif type(index_src) == int:
        #2nd open of the file to delete data
        temp = data_list.pop(index_src)
        print("verification poped:",temp)
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt)