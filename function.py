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

def addBook(file:str,name:str=None):
    """function to add a book at the end of the file
    file: the file un want to read (.txt)
    name: the name of the book you want to append"""
    if name != None:
        name = str(input("Entrez le titre du livre à ajouter : "))
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


def delete_Book(file:str,file2:str):
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
            l2 = ligne.strip('\n')
            print(l2," et ", name)
            if l2 != name:
                data_list.append(l2)
                #print(index_src, "index src")
            else:
                index_src = content.index(ligne)+1 #attention au + 1 avc le décalage mais c possible que pb apres
                print("verif finding",ligne,index_src)

    #condition verification
    if index_src == None :
        return(print("Ce livre n'est pas dans la base donnée"))
    elif index_src != None:
        #2nd open of the file to delete data
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt+'\n')

        #delete occurences in booksread
        with open(file2, "r", encoding='utf-8') as f2:
            # read open file
            content = f2.readlines()
            index_src = 2
            print("content",content)
            for elt in content:
                tmp = elt.split(',')
                print(type(tmp))
                print("ligne et tmp",ligne,tmp)
                for elt2 in tmp[1:]:
                    if int(elt2) == int(index_src):
                        print("tmp avant pop",tmp)
                        tmp.pop(tmp.index(elt2))
                        print("tmp apres pop",tmp)
                data_list.append(tmp)

        # with open(file2, "w", encoding='utf-8') as f2:
        #     # write new data open file
        #     for elt in data_list:
        #         data_list=[]
        #         f2.write(elt+'\n')

def Booksread_update(file):
    """create a folder with each reader"""
    data_list=[]
    tmp=[]
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            tmp=ligne.split(',')
            print("ligne",ligne)
            print("tmp", tmp)
            data_list.append(tmp[1])

    with open(file, "w", encoding='utf-8') as f2:
        f2.readline()
        f2.write

        readers.write(str(Genre)+" ,")
        # age : en dessous de 18 ans , 18-25 ans  et + de 25 ans
        Age = int(input("Rentrer votre âge : "))
        match Age:
            case Age if Age < 18:
                print("Vous avez en dessous de 18 ans.")
                Age = 1
            case Age if Age >= 18 and Age <= 25 :
                print("Vous avez entre 18 et 25 ans.")
                Age= 2
            case Age if Age > 25 :
                print("Vous avez au dessus de 25 ans")
                Age = 3
        readers.write(str(Age)+" ,")
        Style = int(input("Rentrer 1 si vous aimer la Science-fiction,\nRentrer 2 si vous aimer la Biographie,\nRentrer 3 si vous aimer l'Horreur,\nRentrer 4 si vous aimer la Romance,\nRentrer 5 si vous aimer les Fables,\nRentrer 6 si vous aimer l'Histoire,\nRentrer 7 si vous aimer la Comédie : "))
        readers.write(str(Style)+"\n")
    pass