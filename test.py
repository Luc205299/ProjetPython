Matrix1 = [[1,3,5],[9,8,7],[7,8,9],[4,6,7]]

"""def save_matrix(file,m):
    #global Matrix
    with open(file,"w") as f:
        for i in range(len(m)):
            f.write(str(m[i])+"\n")
    return m
print(len(Matrix1))
print(Matrix1[1])
save_matrix("Matrix.txt",Matrix1)"""


"""def import_matrix(file):
    n = []
    with open(file, "r", encoding='utf-8') as f:
        line = f.readlines()
        # read the file
        for i in range(len(line)):
            print("line      : ",len(line))
            L = []
            if i == 0:
                # tmp=[]
                tmp = line[i].strip(',\n').split(",")
                print("tmp= ",tmp)
                L = tmp
            else:
                a = line[i].strip(',\n').split(",")
                for j in range(len(a)):
                    # print("a =",a)
                    if j == 0:
                        # ajouter le premier elt de la liste
                        L.append(a[0])
                    else:
                        print("a       : ",a)
                        a = line[i].strip('\n').split(",")
                        print("\na mofif : ", a,"\n")
                        print("a[j]   =",a[j],j)
                        L.append(a[j])
                        print("L    =",L)
            n.append(L)
    return n


a=import_matrix("Matrix.txt")
print(a)"""
"""P=[]
with open("Matrix.txt","r") as f :
    line=f.readline()
    L = []
    while line != "":

        a=line.strip("\n").strip(' [ ').strip(' ]')
        print("A = ",a, len(a))
        a=list(map(str, a))
        for i in a:

            if 58 > ord(i) > 48:
                print(i)
                L.append(i)
            print("L : ",L)
            results = [int(i) for i in L]
            print("res    =     : ",results)
        P.append(results)
        line = f.readline()
        L=[]
        print("PPPPPP    =", P)"""








"""        print(type(a))
        #print(type(b))
        P.append(a)"""


"""
        m.append(line.strip("\n"))
        line = f.readline()
    for elt in line:
        a=elt.strip('\n').split()
        print(type(a))
        """
"""Matrix2 = [[1,3,5],[9,8,7],[7,8,9]]
b = list(map(str, Matrix2))
print(b)
int_list = [float(i) for i in b]
print(int_list)

x = ['0.58', '0.69', '0.48']
b2 = list(map(str, x))
print(b2)
results = [float(i) for i in x]
print(results)
"""



print(username_ascii("AZERTYUIOPQ5DFGHJKLMWXCVBN"))