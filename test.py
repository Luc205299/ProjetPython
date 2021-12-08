Matrix1 = [[1,3,5],[9,8,7],[7,8,9]]

def save_matrix(file,m):
    #global Matrix
    with open(file,"w") as f:
        for i in range(len(m)):
            f.write(str(m[i])+"\n")
    return m
print(len(Matrix1))
print(Matrix1[1])
save_matrix("Matrix.txt",Matrix1)


def import_matrix(file,m):
    #global Matrix
    with open(file,"r") as f :
        line=f.readlines()
        while line != "":
            m.append(line.strip("\n"))
            line=f.readline()


#import_matrix(f"Matrix.txt",Matrix1)
#print(Matrix1)
P=[]
with open("Matrix.txt","r") as f :
    line=f.readlines()
    print(line)
    for elt in line:
        a=elt.strip('\n').split()
        print(type(a))
        P.append(a)
        print(P)

