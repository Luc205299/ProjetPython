""" Book recommandation project, programming in python

    Sylvan Buhard
    Lucas Barthelemy
    matrix_simi.py: create and use the matrix that calculate the similarity between two profile
     and use it to suggest a book"""

# importations needed
from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *


def init_matrixSimi(file:str, file2:str):
    """init the matrix used to show the percentage of compatibility between each and every reader
    :param  file 1:matrix_simi.txt
    :param file 2: matrix.txt
    :return nothing, the matrix ius directly saved in the file1"""
    Matrix_simi=[]
    matrix1 = import_matrix(file2)
    if len(matrix1) < 1:
        return print("Not enough profiles on the app to get a suggestion.")
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
                # if one sum is equal to 0, compatibility will be 0, avoid zero division error
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


def book_suggestion(file1:str, file2:str, file3:str, file4:str, name: str):
    """suggest a book nased on the matrix_simi
    -file1 : readers.txt
    -file2 : Matrice_similarité.txt
    -file3 : booksread.txt
    -file4 : books.txt
    -name : name of the user
    return : str depedning on the case"""
    # test if the user is connected with an existing pseudo
    if not users_exist(file1, name):
        return print("Please, register before making this query.")
    if is_empty(file2) is True:
        return print("Not enough profiles on the application, invite your friends ;)")
    matrix = import_matrix(file2)
    # transform each str note to int an int value
    for line in range(1, len(matrix)):
        for row in range(1, len(matrix[line])):
            matrix[line][row] = float(matrix[line][row])

    # search for the line of the user
    for line in range(1, len(matrix)):
        if matrix[line][0] == name:
            user_line = matrix[line]

    # deduce the person the most similar to the given name byb grabbing the number of column
    sibling = matrix[0][user_line.index(max([0 if elt == 1 else elt for elt in user_line[1:]]))]
    # show books that the sibling has read
    with open(file3, "r", encoding='utf-8') as bksr:
        # list of every line in booksread
        line_bksr = [elt.strip('\n').split(",") for elt in bksr.readlines()]
        # list of every line number of books in the sibling profile
        line_number = []
        # search the line with the same noun as the sibling in every line
        for elements in line_bksr:
            # elements is th list of reader one by one
            if elements[0].strip(" ") == sibling:
                linebksr_sibling = elements
            elif elements[0].strip(" ") == name:
                linebksr_user = elements
        # add every book that hasn't been read yet by their index
        for elt in linebksr_sibling[1:]:
            if elt not in linebksr_user[1:]:
                if elt != '':
                    line_number.append(int(elt))
        # go through every book to add it
        with open(file4, "r", encoding='utf-8') as bks:
            # transform every book index into the title
            temp = [elt.strip('\n') for elt in bks.readlines()]
            line_bks = [temp[elt] for elt in line_number]
        if len(line_bks) == 0:
            return print("Sadly, no recommendations are possible, your have read every book we could have suggested.")
        else:
            print("Here's our personal suggestions : \n")
            for elt in line_bks:
                print(f"- {elt}")
    # input the concerned book
    choice = str(input("Choose one : "))
    while choice not in line_bks:
        choice = str(input("Please, pick one that u see in the following line :"))
        print(line_bks)
    # after the user chose a new among suggestions books
    booksread_addBook(file1, file4, file3, name, choice)
    answer = str(input("Do you want to rate it ? ( y / n ):"))
    if answer == "y":
        fm.update_Matrix(file4, file3, name, choice)
    else:
        # reminder to note the book
        return print(f"Do not forget to rate {choice} after you finished !")