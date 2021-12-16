from FunctionMatrix import *
import FunctionMatrix as fm
from function import *
from math import *
from functionUsers import *

Matrix_simi = []


def init_matrixSimi(file, file2):
    """init the matrix used to show the percentage of compatibiity and sameness between each and every reader
    file : readers.txt
    file 2: matrix"""
    global Matrix_simi
    Matrix1 = import_matrix(file2)
    # transform each str note to int an int value
    for line in range(1, len(Matrix1)):
        for row in range(1, len(Matrix1[line])):
            Matrix1[line][row] = int(Matrix1[line][row])
    # add readers list as first line
    Matrix_simi.append([Matrix1[i][0] for i in range(len(Matrix1))])
    # append each reader to the head of each line initialized with 0
    for i in range(1, len(Matrix1)):
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
                a = Matrix1[i][1:]
                b = Matrix1[j][1:]
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


# init_matrixSimi("Matrice_similarité.txt", "Matrix.txt")


def book_suggestion(file1, file2, file3, file4, name):
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
    print("test", matrix)
    # transform each str note to int an int value
    for line in range(1, len(matrix)):
        for row in range(1, len(matrix[line])):
            matrix[line][row] = float(matrix[line][row])

    # search for the line of the user
    for line in range(1, len(matrix)):  # remplacer par un while
        if matrix[line][0] == name:
            print(f"trouvé !, line = {matrix[line]}")
            user_line = matrix[line]

    # deduce the person the most similar to the given name byb grabbing the number of column
    sibling_index = user_line.index(max([0 if elt == 1 else elt for elt in user_line[1:]])) # a optimiser
    sibling = matrix[0][sibling_index]
    print("trouvé sibling = ", sibling)

    # show books that the sibling has readen
    with open(file3, "r", encoding = 'utf-8') as bksr:
        # list of every line in booksread
        line = bksr.readlines()
        print("line =", line)
        # list of every line numbe rof books
        line_number = []
        # search the line with the same noun as the sibling in evrey line
        for elt in line:
            # elements is th list of reader one by one
            elements = elt.strip('\n').split(",")
            print("elements", elements)
            print(elements[0], " == ?", sibling)
            if elements[0] == sibling:
                line_number = [int(elt) for elt in elements[1:]]
                print("test", elements, '\n', line_number)
        # go through every book to add it
        with open(file4, "r", encoding='utf-8') as bks:
            # list of read books by the sibling presnted at the end
            line_bks = []
            # list of all books
            listebook = [elt.strip('\n') for elt in bks.readlines()]

            print("try", listebook, '\n', elements)
            # for each number in element
            for elt in line_number:
                line_bks.append(listebook[elt])
        print(" voici les livres qui son susceptibles de vous plaire; ")
        print(line_bks)
        # imprime la liste des livres
    # imput the concerned book
    chc = str(input("Choissisez en un : "))
    while chc not in line_bks: # a changer avec l'index !!!
        chc = str(input("Veuillez en choisir un parmi tous ceux là :"))
        print(line_bks)
    #print("chc", chc)
    # after the user chose a book
    booksread_addBook(file1, file4, file3, name, chc)
    answer = str(input("voulez vous le noter? (si vous l'avez déja lu) ( y / n )"))
    if answer == "y":
        fm.update_Matrix(file4, file3, name, chc)
    else:
        # reminder to note the book
        return print("N'oubliez pas de le noter quand vous aurez fini !")


book_suggestion("readers.txt", "Matrice_similarité.txt", "booksread.txt", "Books.txt", "table")