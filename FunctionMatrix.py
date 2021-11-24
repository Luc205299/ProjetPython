def IniMatrix(file1,file2):
    Matrix=[]
    with open(file1, "r") as readers:
        cpt1=0
        line = readers.readline()
        while line != "":
            cpt1+=1
            line = readers.readline()
    with open(file2, "r") as books:
        cpt2=0
        line = books.readline()
        while line != "" :
            cpt2+=1
            line = books.readline()
        print(cpt1,cpt2)
    for line in range(cpt1):
        L=[]
        for rows in range(cpt2):
            L.append(0)
        Matrix.append(L)
    return Matrix


