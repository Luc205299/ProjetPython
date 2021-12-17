from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *


def is_empty(file) -> bool:
    """return true if a folder is empty"""
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        content = f.readlines()
        # if file is empty, return True
        if len(content) == 0:
            return True
    #else return false
    return False


def ShowBook(file: str):
    """function to open and read the Books file and print what's inside
    file: the file un want to read (.txt)
    listing: list of books to show, and not the others"""

    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
    # print every book in the folder, with it number
    for count, content in enumerate(content):
        print(count, ":", content)
    return print("\n")


def book_exist(file1, name):
    """function to search if a book exist and return it number if it is true
    file: the file un want to read (.txt)
    name: the name of the book you want to look for"""

    exist = None
    # open file in read mode
    with open(file1, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            ligne2 = ligne.strip('\n')
            if ligne2 == name:
                exist = True
                return content.index(ligne)

    if exist == None:
        return None


def addBook(file: str, file2: str, name: str = None):
    """function to add a book at the end of the file
    file: book (.txt)
    file2: matrix.txt
    name: the name of the book you want to append"""
    if name != None:
        name = str(input("Entrez le titre du livre à ajouter : "))
    exist = book_exist(file, name)

    if exist == False:
        j = open(file, "a", encoding='utf-8')
        j.write(name)
        j.close()
    else:
        return print("il existe déja")
    # append it at the end of matrix
    matrix = fm.import_matrix(file2)
    matrix[0].append(name)
    for i in range(len(matrix) - 1):
        matrix[i].append('0')

    print("le livre a bien été ajouté, et la amtrice mise a jour")
    fm.save_matrix(file, matrix)


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
        # 2nd open of the file to modify data
        new_title = str(input("Quel est le nouveau titre de ce livre?"))
        data_list[index_src] = new_title
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt)


def saisir_livres(file1: str = None) -> bool:  # a squoi sa sert
    """ne fais rien et n'est pas utilisé
    file1 : file.txt permet d'apcceder au dossier en question"""
    L = []
    stop = False
    with open(file1, "a") as bookread:
        while not stop:
            read = int(input("saisissez le livre avez vous lus"))
            bookread.write("," + str(read) + " ")
            verification = str(input("Avez vous d'autre livres à Saisir ? ( yes / no) :"))
            if verification == "no":
                stop = True


def delete_Book(file: str, file2: str):
    """ delete an existing book from the repository/library of file in argument
    file: str the file in question
    file : books.txt
    file2: booksread"""
    # condition verification if the book exist
    global Matrix
    name = str(input("Entrez le titre du livre à supprimer :"))
    position = book_exist(file, name)
    if position == None:
        return print("Ce livre n'est pas dans la base donnée")
    # list of file data
    data_list = []

    # delete the line linked to the book index in the matrix
    for line in Matrix:
        print(f"matrix avant :\n {Matrix}")
        line.pop(position)
        print(f"matrix après :\n {Matrix}")

    # delete occurrences in booksread
    with open(file2, "r", encoding='utf-8') as f2:
        # read open file to search the book occurences
        content = f2.readlines()
        for elt in content:
            tmp = elt.strip('\n').split(',')
            for elt2 in tmp[1:]:
                # rewrite every value of books minus one, because it has to fill the hole
                if int(elt2) > position:
                    # print("elt2 :", elt2, type(elt2))

                    tmp[tmp.index(elt2)] = str(int(elt2) - 1)

                elif int(elt2) == position:
                    tmp.pop(tmp.index(elt2))
            print(f"il va donc append {tmp}")
            # rewrite every element in the line separated by a coma
            data_list.append(tmp)

    # rewrite data in the file without the deleted one
    with open(file2, "w", encoding='utf-8') as f:
        # write new data open file
        for elt in data_list:
            for elt2 in elt:
                if elt.index(elt2) == 0:

                    f.write(elt2)
                else:
                    f.write(" ," + elt2)
            f.write('\n')

    # delete in books.txt
    data_list = []
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            l2 = ligne.strip('\n')
            if l2 != name:
                data_list.append(l2)
            else:
                index_src = content.index(ligne)  # attention au + 1 avc le décalage mais c possible que pb apres
    # 2nd open of the file to rewrite data with correct list of readed books
    with open(file, "w", encoding='utf-8') as f:
        # write new data in openend file
        for elt in data_list:
            f.write(elt + '\n')


def booksread_verify(file1, file2, reader, title):
    """verify is a book as been read by the reader
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
        # print("content", content)
        for ligne in content:
            # print("ligne =", ligne)
            l2 = ligne.strip(',\n').strip('').split(',')
            # print("l2=", l2)
            # verify if the book is already written
            if l2[0] == reader:
                # if found, stop the process with return function, from the second elt in list
                for elt in l2[1:]:
                    # may pose pb with the end of line with \n
                    # print("elt==", elt, "position", position)
                    if int(elt) == int(position):
                        # print("Vous avez bien lu ce livre")
                        return True, position
        return False


def booksread_addBook(file, file1, file2, reader, title=None):
    """update the folder with each reader and the books he has readen
    file: readers
    file1: books
    file2: booksread
    reader, the currently logged user"""
    # verifiy is the user is connected
    if users_exist(file, reader) == False:
        return print("erreur nom d'utilisateur, prière de vous connecter avec un identifiant valide")
    # title of the book for identification
    if title == None:
        #
        title = str(input("Entrez le titre du nouveau livre que vous avez lu :"))
    test = book_exist(file1, title)
    if test == None:
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
                    elt2 = str(elt.strip(" "))
                    if str(elt2) == str(position):
                        return print("Vous avez déjà entré ce livre")
                # if not written, add position related to the book at the end of the line, and separated byt a coma
                l3 = ligne.strip(',\n')
                print("l3 avant ", l3)
                l3 = l3 + "," + str(position) + '\n'
                data_list.append(l3)
                print("l3 avant ", l3, "\ndata", data_list)
            else:
                data_list.append(ligne)

    # 2nd open of the file to rewrite data with correct list of readed books
    with open(file2, "w", encoding='utf-8') as f:
        # write new data in openend file
        # print("datalist",data_list)
        for elt in data_list:
            # print("elt =", elt)
            f.write(elt)
    print("vous avez bien ajouté le livre a la liste des lus")
