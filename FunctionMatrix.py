from function import *

Matrix = []


def init_Matrix(file1, file2, file3=None):
    """create a matrix with books as columns, persons as rows
    file1: books.txt
    file2: matrix.txt
    file3: readers.txt optionnal"""
    global Matrix
    # append the book line as the line[0] in the matrix
    with open(file2, "r", encoding='utf-8') as f:
        line = f.readlines()
        # if the folder isn't empty
        if len(line) != 0:
            # if already initialized, import the matrix from the file
            Matrix = import_matrix(file2)

        # if the folder is empty
        else:
            # import first line of the matrix with
            with open(file1, "r", encoding='utf-8') as bks:
                line = bks.readlines()
                tmp = ["0"]
                for elt in line:
                    tmp.append(elt.strip("\n"))
                Matrix.append(tmp)
            # import each line to init from readers in case of many readers but 0 notes
            with open(file3, "r", encoding='utf-8') as f2:
                # for each reader in the folder
                line = f2.readlines()
                tmp_final = []
                for elt in line:
                    tmp = [i - i for i in range(len(Matrix[0]) - 1)]
                    tmp[0] = elt.strip("\n").split(",")[0]
                    # update matrix folder
                    save_matrix(file2, Matrix)
                    tmp_final.append(tmp)
                for elt in tmp_final:
                    Matrix.append(elt)


def update_Matrix(file1, file2, reader, book=None) -> list:
    """update the matrix with notes of the reader
    file1: books.txt
    file2: booksread.txt
    reader: the logged user"""
    #global Matrix
    Matrix = import_matrix("Matrix.txt")
    #Matrix = matrix
    if book == None:
        book = str(input("Entrez le titre du livre a noter :"))
    # if the book exist and has already been readen
    test = booksread_verify(file1, file2, reader, book)
    print("test =", test)
    if test[0] == True:
        position = test[1]
        note = 0
        while note <= 0 or note > 5:
            note = int(input("Veuillez entrer votre note, entre 1 et 5 : "))

    elif test[0] == False:
        return print("Veillez lire le livre en question avant de le noter.")
    else:
        return print(test)
    cpt = 0
    # first elt of each column is a reader, the first line books
    print("verif : ", Matrix[cpt][0] == reader)
    while Matrix[cpt][0] != reader or Matrix[cpt][0] == None:  # ! need the name of the user with OONE space after,
        # match format
        print(f"tentative {cpt}, user = {reader} =  {Matrix[cpt][0]} donc {Matrix[cpt][0] == reader}")
        cpt += 1
    # update matrix in related position
    Matrix[cpt][position] = note
    # verification of the good changes
    print("Matrice:")
    for line in Matrix:
        print(line)
    # met a jour la matrice avec la nouvelle note
    save_matrix("Matrix.txt", Matrix)
    return Matrix


def save_matrix(file, Matrix):
    # global Matrix
    with open(file, "w", encoding='utf-8') as f:
        # print("Matrix",len(Matrix), '\n',Matrix)
        for i in range(len(Matrix)):

            # print("i =",i)
            for j in range(len(Matrix[i])):
                # print("j =",j)
                f.write(str(Matrix[i][j]) + ",")
            f.write("\n")


def import_matrix(file):
    n = []
    with open(file, "r", encoding='utf-8') as f:
        line = f.readlines()
        # read the file
        for i in range(len(line)):
            L = []
            if i == 0:
                tmp = line[i].strip(',\n').split(",")
                L = tmp
            else:
                a = line[i].strip(',\n').split(",")
                for j in range(len(a)):
                    if j == 0:
                        L.append(a[0])
                    else:
                        a = line[i].strip('\n').split(",")
                        L.append(a[j])
            n.append(L)
    return n
