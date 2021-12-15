from FunctionMatrix import *
import FunctionMatrix as fm
from math import *

Matrix_simi = []


def init_matrixSimi(file, Matrix):
    """file : readers.txt"""
    global Matrix_simi
    # add every reader in the line and rows
    tmp_list = ['0']
    for line in Matrix:
        # every name is append on the list
        tmp_list.append(line[0])
    # add names as the first line
    Matrix_simi.append(tmp_list)

    tmp_list = ['0']
    for i in range(len(Matrix) - 1):
        # add every name as first element in the matrix for each name, same row has line n°
        Matrix_simi[i][0] = Matrix_simi[0][i]
        for j in range(len(Matrix) - 1):
            if i == j:
                Matrix_simi[i][j] = 1
            else:
                a = Matrix[i]
                b = Matrix[j]
                num = sum(a) * sum(b)  # multiplication ??????
                denom = sqrt(sum(a) ** 2) * sqrt(sum(b) ** 2)
                res = num / denom
                print(res)
                Matrix_simi[i][j] = res

        Matrix_simi.append(tmp_list)
    save_matrix(file, Matrix_simi)


init_matrixSimi("Matrice_similarité.txt")


def book_suggestion(file):
    """suggest a book nased on the similaritude matrix"""  # optimisation: fr jusqu'au prenom déja existante donc fct update matrix
    pass
