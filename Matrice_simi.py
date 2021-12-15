from FunctionMatrix import *
import FunctionMatrix as fm
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


init_matrixSimi("Matrice_similarité.txt", "Matrix.txt")


def book_suggestion(file1, file2, file3, name):
    """suggest a book nased on the similaritude matrix
    # -file1 : readers.txt
    # -Matrix : Matrice_similarité.txt
    # -file3 : booksread.txt
    # -name : name of the user"""
    # optimisation: fr jusqu'au prenom déja existante donc fct update matrix*
    exist=users_exist(file3, name)
    for line in range(1,len(Matrix)+1):
        for rows in range(1,len(Matrix[i])):
            a=None
    pass
