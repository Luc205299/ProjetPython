def init_Matrix(file1,file2):
    """create a matrix with books as columns, persons as rows"""
    Matrix = []
    #append the book line as the line[0] in the matrix
    with open(file1, "r", encoding='utf-8') as bks:
        line = bks.readlines()
        tmp = []
        for elt in line:
            tmp.append(elt.strip("\n"))
        Matrix.append(tmp)

    with open(file2, "r", encoding='utf-8') as readers:
        line = readers.readlines()
        for elt in line:
            tmp = elt.split(',')
            temp_list = [i-i for i in range(len(Matrix[0]))]
            temp_list[0] = tmp[0]
            Matrix.append(temp_list)

    print("Matrice:")
    for line in Matrix:
       print(line)