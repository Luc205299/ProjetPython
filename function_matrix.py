from function_books import *

Matrix = []


def init_Matrix(file1, file2, file3=None):
    """create a matrix with books as columns, persons as rows
    file1: books.txt
    file2: matrix.txt
    file3: readers.txt optional, to create the matrix straight from the reader file """
    global Matrix
    # append the book line as the line[0] in the matrix
    if not is_empty(file2):
        # if the file isn't empty, import the matrix from the folder
        Matrix = import_matrix(file2)
    # if the folder is empty
    else:
        # import first line of the matrix with
        with open(file1, "r", encoding='utf-8') as bks:
            line = bks.readlines()
            tmp = ["0"]
            # create the books line of index 0
            for elt in line:
                tmp.append(elt.strip("\n"))
            Matrix.append(tmp)
        save_matrix(file2, Matrix)
        # import each line to init from readers in case of many readers but 0 notes
        if file3 is not None:
            with open(file3, "r", encoding='utf-8') as f:
                # for each reader in the folder
                line = f.readlines()
                tmp_final = []
                for elt in line:
                    tmp = [i - i for i in range(len(Matrix[0]))]
                    tmp[0] = elt.strip("\n").split(",")[0]
                    # update matrix folder
                    save_matrix(file2, Matrix)
                    tmp_final.append(tmp)
                for elt in tmp_final:
                    Matrix.append(elt)


def update_Matrix(file1, file2, reader, book=None) -> list:
    """update the matrix with note of the reader
    file1: books.txt
    file2: booksread.txt
    reader: the logged user"""
    # global Matrix
    matrix = import_matrix("matrix.txt")
    # Matrix = matrix
    if book is None:
        book = str(input(" What is the title of the book you want to rate :"))
    # if the book exist and has already been read
    if not book_exist(file1, book):
        return print(f" {book} doesn't exist, try to add it before.")
    test = booksread_verify(file1, file2, reader, book)
    if test[0] is True:
        position = test[1]
        note = 10
        while note <= 0 or note > 5:
            note = int(input("Enter your grade, from 1 star to 5 : "))
    elif test[0] == False:
        return print("Please, be aware that you need to read the book before.", test)
    else:
        return print(test)
    cpt = 0
    # first elt of each column is a reader, the first line books
    while matrix[cpt][0] != reader or matrix[cpt][0] is None:
        # match the right line
        cpt += 1
    # update matrix in related position
    matrix[cpt][position] = note
    # update the matrix
    save_matrix("Matrix.txt", matrix)
    return matrix


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
