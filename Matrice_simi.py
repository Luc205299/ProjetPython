from FunctionMatrix import *
import FunctionMatrix as fm
from math import *
from functionUsers import*


Matrix_simi = []


def init_matrixSimi(file, file2):
    """file : readers.txt
    file 2: matrix"""
    global Matrix_simi
    Matrix1 = import_matrix(file2)
    print("Matrix 1",Matrix1)
    # add readers list as first line
    Matrix_simi[0] = Matrix1
    # append each reader to the head of each line initialized with 0s
    for i in range(1,len(Matrix1)):
        # minus one because the book line isn't compted in
        tmp=[j-j for j in i]
        tmp[0]=Matrix_simi[0][i]
        print("tmp",tmp)

        Matrix_simi.append(tmp)
    print("Matrix_simi",Matrix_simi)
    for i in range(len(Matrix_simi)):
        for j in range(len(Matrix_simi)):
            # each person is the most seemblings to himself
            if i == j:
                Matrix_simi[i][j] = 1
            elif i > j:
                Matrix_simi[i][j]=Matrix_simi[j][i]
            else:
                #two lines to compare, without the pseudo
                sum1,sum2 = 0,0
                a = Matrix1[i][1:]
                b = Matrix1[j][1:]
                print(f"a est = {a}\n b est = {b}")
                for k in range(len(a)):
                    sum1+= a[k]**2
                    sum2+=b[k]**2
                if sum1 == 0 or sum2 == 0:
                    Matrix_simi[i][j] = 0
                else:
                    num=0
                    for m in range(len(a)):
                        num += a[m]*b[m]
                    denom = sqrt(sum1)*sqrt(sum2)
                    Matrix_simi[i][j] = round(num/denom,2)



    save_matrix(file, Matrix_simi)


init_matrixSimi("Matrice_similarité.txt","Matrix.txt")


def book_suggestion(file1,file2,file3,name):
    """suggest a book nased on the similaritude matrix
    # -file1 : readers.txt
    # -Matrix : Matrice_similarité.txt
    # -file3 : booksread.txt
    # -name : name of the user"""
    # # optimisation: fr jusqu'au prenom déja existante donc fct update matrix*
    # exist=users_exist(file3, name)
    # for line in range(1,len(Matrix)+1):
    #     for rows in range(1,len(Matrix[i])):
    #         a=




