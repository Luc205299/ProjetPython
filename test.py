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


def import_matrix(file,m):
    #global Matrix
    m = []
    print(m)
    n=m
    with open(file, "r") as f:
        line = f.readline()
        L = []
        while line != "":
            print("j",line)
            a = line.strip("\n").strip(' [ ').strip(' ]')
            print("A = ", a, len(a))
            a = list(map(str, a))
            for i in a:

                if 58 > ord(i) > 47:
                    print(i)
                    L.append(i)
                    results = [int(i) for i in L]
                    print("L : ", L)
                print("res    =     : ", results)
            n.append(results)
            line = f.readline()
            L = []
            print("PPPPPP    =", n)
    return n

n=[]
import_matrix(f"Matrix.txt",n)
print(n)
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

