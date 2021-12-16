from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *

Matrix_simi = []


def init_matrixSimi(file, file2):
    """init the matrix used to show the percentage of compatibiity and sameness between each and every reader
    file : readers.txt
    file 2: matrix"""
    global Matrix_simi
    matrix1 = import_matrix(file2)
    # transform each str note to int an int value
    for line in range(1, len(matrix1)):
        for row in range(1, len(matrix1[line])):
            matrix1[line][row] = int(matrix1[line][row])
    # add readers list as first line
    Matrix_simi.append([matrix1[i][0] for i in range(len(matrix1))])
    # append each reader to the head of each line initialized with 0
    for i in range(1, len(matrix1)):
        tmp = [j - j for j in range(len(Matrix_simi[0]))]
        tmp[0] = Matrix_simi[0][i]
        Matrix_simi.append(tmp)
    # assign a value to each case of the matrix
    for i in range(1, len(Matrix_simi)):
        for j in range(1, len(Matrix_simi)):
            # each person as a 100% with himself
            if i == j:
                Matrix_simi[i][j] = 1
            # fill half the matrix with calculus method, the other half is a copy, since the matrix is symmetric
            elif i > j:
                Matrix_simi[i][j] = Matrix_simi[j][i]
            else:
                # two compared lines, without the pseudo
                sum1, sum2 = 0, 0
                a = matrix1[i][1:]
                b = matrix1[j][1:]
                # compare each value of the line with every other of the same column
                for k in range(1, len(a)):
                    sum1 += a[k] ** 2
                    sum2 += b[k] ** 2
                # if one sum is equal to 0, compatibility will be 0
                if sum1 == 0 or sum2 == 0:
                    Matrix_simi[i][j] = 0
                else:
                    num = 0
                    # calculus of the compatibility percentage
                    for m in range(len(a)):
                        num += a[m] * b[m]
                    denom = sqrt(sum1) * sqrt(sum2)
                    Matrix_simi[i][j] = round(num / denom, 2)
    # save the matrix in the linked file
    save_matrix(file, Matrix_simi)


def book_suggestion(file1, file2, file3, file4, name: str):
    """suggest a book nased on the matrix_simi
    -file1 : readers.txt
    -file2 : Matrice_similarité.txt
    -file3 : booksread.txt
    -file4 : books.txt
    -name : name of the user"""
    # optimisation: fr jusqu'au prenom déja existante donc fct update matrix*

    # test if the user is connected with an existing pseudo
    # exist = users_exist(file1, name)
    # if exist == False:
    #     return print("Veuillez vous inscrire d'abord")

    matrix = import_matrix(file2)
    # transform each str note to int an int value
    for line in range(1, len(matrix)):
        for row in range(1, len(matrix[line])):
            matrix[line][row] = float(matrix[line][row])

    # search for the line of the user
    for line in range(1, len(matrix)):  # remplacer par un while
        if matrix[line][0] == name:
            user_line = matrix[line]

    # deduce the person the most similar to the given name byb grabbing the number of column
    sibling = matrix[0][user_line.index(max([0 if elt == 1 else elt for elt in user_line[1:]]))]

    # show books that the sibling has readen
    with open(file3, "r", encoding='utf-8') as bksr:
        # list of every line in booksread
        line_bksr = [elt.strip('\n').split(",") for elt in bksr.readlines()]
        # list of every line number of books in the sibling profile
        line_number = []
        # search the line with the same noun as the sibling in every line
        for elements in line_bksr:
            # elements is th list of reader one by one
            if elements[0] == sibling:
                linebksr_sibling = elements
            elif elements[0] == name:
                linebksr_user = elements

        # add every book that hasn't been readen yet by their index
        for elt in linebksr_sibling[1:]:
            if elt not in linebksr_user[1:]:
                line_number.append(int(elt))

        # go through every book to add it
        with open(file4, "r", encoding='utf-8') as bks:
            # list of all books
            listebook = [elt.strip('\n') for elt in bks.readlines()]
            # transform every book index into the title
            line_bks = [listebook[elt] for elt in line_number]
        if len(line_bks) == 0:
            print("Malheureusement, aucun livre ne peut vous etre suggerer, vous etes clui qui a le plus lu de livres")
        else:
            print("Voici le(s) livre(s) susceptibles de vous plaire: ")
            print(*line_bks)

    # imput the concerned book
    chc = str(input("Choissisez en un : "))
    while chc not in line_bks: # a changer avec l'index !!!
        chc = str(input("Veuillez en choisir un parmi tous ceux là :"))
        print(line_bks)
    # after the user chose a book
    booksread_addBook(file1, file4, file3, name, chc)
    answer = str(input("voulez vous le noter? ( y / n ):"))
    if answer == "y":
        fm.update_Matrix(file4, file3, name, chc)
    else:
        # reminder to note the book
        return print("N'oubliez pas de le noter quand vous aurez fini !")