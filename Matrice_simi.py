from FunctionMatrix import *
from math import *

Matrix_simi = []


def init_matrixSimi(file):
    """file:readers.txt"""
    global Matrix, Matrix_simi
    # add every reader in the line and rows
    for line in Matrix:
        tmp_list = [0]
        for elt in line:
            # every name
            tmp_list.append(elt)
    Matrix.append(tmp_list)

    for i in range(len(Matrix) - 1):
        # add every name as first in the matrix
        tmp_list[0] = Matrix[0][i]
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

        tmp_list.append(tmp_list)
    save_matrix(file, Matrix_simi)


def book_suggestion(file):
    """suggest a book nased on the similaritude matrix"""  # optimisation: fr jusqu'au prenom déja existante donc fct update matrix
    pass
