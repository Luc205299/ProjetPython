"""Created on Mon Apr 12 13:19:47 2021

@author: Buhard
"""


def ShowBook(file: str):
    """function to open and read the Books file and print what's inside
    file: the file un want to read (.txt)"""
    # open file in read mode
    with open(file, "r") as f:
        # read open file
        content = f.readlines()
    cpt = 1
    for line in content:
        print(cpt, ":", str(line), '\n')
        cpt += 1
    return ()


def book_exist(file1, name):
    """function to search if a book exist and return it number if it is true
    file: the file un want to read (.txt)
    name: the name of the book you want to look for"""

    exist = False
    # open file in read mode
    with open(file1, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            ligne2 = ligne.strip('\n')
            if ligne2 == name:
                exist = True
                return content.index(ligne)

    if exist == False:
        return (False)


def addBook(file: str, name: str = None):
    """function to add a book at the end of the file
    file: the file un want to read (.txt)
    name: the name of the book you want to append"""
    if name != None:
        name = str(input("Entrez le titre du livre à ajouter : "))
    exist = False
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            ligne2 = ligne.strip('\n')
            # print("ligne2 :", ligne, " and ", name, ("?"))
            if ligne2 == name:
                print("Ce livre est déjà dans le dépôt")
                exist = True

    if exist == False:
        j = open(file, "a", encoding='utf-8')
        j.write(name)
        j.close()


def changeTitle(file: str):
    """function to modify an existing book in file
    file: the file un want to read (.txt)
    name: the name of the book you want to modify"""

    name = str(input("Entrez le titre du livre à modifier :"))
    index_src = None
    # list of file data
    data_list = []
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            # print(ligne," et ", name)
            data_list.append(ligne)
            if str(ligne) == name:
                index_src = content.index(ligne)
                # print(index_src, "index src")

    if index_src == None:
        return print("Ce livre n'est pas dans la base donnée")

    elif type(index_src) == int:
        # print("verif ", data_list[index_src])
        # 2nd open of the file to modify data
        new_title = str(input("Quel est le nouveau titre de ce livre?"))
        data_list[index_src] = new_title
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt)


def delete_Book(file: str, file2: str):
    """ delete an existing book from the repository/library of file in argument
    file: str the file in question """

    name = str(input("Entrez le titre du livre à supprimer :"))
    index_src = None
    # list of file data
    data_list = []
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            l2 = ligne.strip('\n')
            print(l2, " et ", name)
            if l2 != name:
                data_list.append(l2)
                # print(index_src, "index src")
            else:
                index_src = content.index(ligne) + 1  # attention au + 1 avc le décalage mais c possible que pb apres
                print("verif finding", ligne, index_src)

    # condition verification
    if index_src == None:
        return print("Ce livre n'est pas dans la base donnée")
    elif index_src != None:
        # 2nd open of the file to delete data
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt + '\n')

        # delete occurences in booksread
        with open(file2, "r", encoding='utf-8') as f2:
            # read open file
            content = f2.readlines()
            index_src = 2
            print("content", content)
            for elt in content:
                tmp = elt.split(',')
                print(type(tmp))
                print("ligne et tmp", ligne, tmp)
                for elt2 in tmp[1:]:
                    if int(elt2) == int(index_src):
                        print("tmp avant pop", tmp)
                        tmp.pop(tmp.index(elt2))
                        print("tmp apres pop", tmp)
                data_list.append(tmp)

        # ajouter le pb des numéros qui vont se décaler lors de la supression, supprimer de la matrice

        # with open(file2, "w", encoding='utf-8') as f2:
        #     # write new data open file
        #     for elt in data_list:
        #         data_list=[]
        #         f2.write(elt+'\n')


def booksread_verify(file1, file2, reader, title):
    """verify is a book as been read byth reader
       file1: books
       file2: booksread
       reader, the currently logged user"""
    # check if the title exist
    test = book_exist(file1, title)
    if test == False:
        return f"Le livre : {title} n'existe pas, essayez de l'ajouter avant."
    else:
        position = test
    # open file in read mode
    with open(file2, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            l2 = ligne.strip('\n')
            l2 = l2.split(',')
            # verify if the book is already written
            if l2[0] == reader:
                # if found, stop the process with return function, from the second elt in list
                for elt in l2[1:]:
                    # may pose pb with the en dof line with \n
                    if int(elt) == int(position):
                        print("Vous avez bien lu ce livre")
                        return True, position
        return False


def booksread_addBook(file1, file2, reader):
    """create a folder with each reader and the books he has readen
    file1: books
    file2: booksread
    reader, the currently logged user"""
    # ask for the new book title
    title = str(input("Entrez le titre du nouveau livre que vous avez lu :"))
    test = book_exist(file1, title)
    if test == False:
        return "Le livre :", title, " n'existe pas, essayez de l'ajouter avant"
    else:
        position = test

    # copy the data in the file before the changes
    data_list = []
    # open file in read mode
    with open(file2, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            l2 = ligne.strip('\n')
            l2 = l2.split(',')
            # verify if the book isn't already written
            if l2[0] == reader:
                # if one is ever found, stop the process with return function
                for elt in l2:
                    if str(elt) == str(position):
                        return print("Vous avez déjà entré ce livre")
                # if not written, add position related to the book at the end of the line, and separated byt a coma
                l3 = ligne.strip('\n')
                l3 = l3 + "," + str(position) + '\n'
                data_list.append(l3)
            else:
                data_list.append(ligne)

    # 2nd open of the file to rewrite data with correct list of readed books
    with open(file2, "w", encoding='utf-8') as f:
        # write new data in openend file
        for elt in data_list:
            print("elt =", elt)
            f.write(elt)
