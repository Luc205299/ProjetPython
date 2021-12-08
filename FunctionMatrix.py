from function import *

Matrix = []


def init_Matrix(file1, file2):
    """create a matrix with books as columns, persons as rows"""
    # import the global matrix
    global Matrix
    # append the book line as the line[0] in the matrix
    with open(file1, "r", encoding='utf-8') as bks:
        line = bks.readlines()
        # useless case in top left corner, filled with a random value
        tmp = ["0"]
        for elt in line:
            tmp.append(elt.strip("\n"))
        Matrix.append(tmp)

    print("Matrice:")
    print(Matrix)
    print("Matrice:")
    for line in Matrix:
        print(line)


def update_Matrix(file1, file2, reader) -> list:
    """update the matrxi wuth notes of every reader
    file1:books
    file2: booksread
    reader: the logged user"""
    global Matrix
    book = str(input("Entrez le titre du livre a noter :"))
    # if the book exist and has already been readen
    test = booksread_verify(file1, file2, reader, book)
    if test[0] == True:
        position = test[1]
        note = 0
        while note <= 0 or note > 5:
            note = int(input("Veuillez entrer votre note, entre 1 et 5 : "))

    elif test == False:
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
    return Matrix

def supress_Matrix(file1, file2, reader) -> list:
    """create a matrix with books as columns, persons as rows
    file1 : books
    file2: booksread
    reader: the logged user"""
    global Matrix
    book = str(input("Entrez le titre du livre a noter :"))
    # if the book exist and has already been readen
    test = booksread_verify(file1, file2, reader, book)
    if test[0] == True:
        position = test[1]
        note = 0
        while note <= 0 or note > 5:
            note = int(input("Veuillez entrer votre note, entre 1 et 5 : "))

    elif test == False:
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
    return Matrix

def save_matrix(file):
    global Matrix
    with open(file,"w") as f:
        for i in range(len(Matrix)):
            f.write(str(Matrix[i])+"\n")