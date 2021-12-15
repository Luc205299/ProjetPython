from FunctionMatrix import *


# Fonction permettant de créer le profil de l'utilisateur avec le nom, le genre , l'age, et le style aimé par l'users !!!TRADUIRE EN ANGLAIS!!! """
def Profil(file, file2, Matrix):
    with open(file, "a") as readers:
        with open(file2, "a") as br:
            Pseudo = str(input("Enter your name : "))
            # Add the username to the file "readers.txt"
            readers.write(Pseudo + ",")
            br.write(Pseudo + " ,\n")

            """cette partie ne fais pas attention aux doublets a refaire"""  # Add the username to the Matrix ne fais pas attention aux doublets

            print("Matrice est =", Matrix)
            print("Matrix 0 =", Matrix[0], '\n', "len(Matrix[0])",len(Matrix[0]))
            temp_list = [i - i for i in range(len(Matrix[0]))]
            print("len=", len(temp_list))
            temp_list[0] = Pseudo
            print(temp_list)
            print("len ", len(temp_list))
            Matrix.append(temp_list)
        Genre = 0
        while Genre <= 0 or Genre > 4:
            Genre = int(input(
                "Si vous êtes un Homme tapez 1 ; \nSi vous êtes une Femme tapez 2 ; \nSi vous souhaitez ne pas rentrer votre genre, tapez 3 : "))
        readers.write(str(Genre) + " ,")
        # age : en dessous de 18 ans , 18-25 ans  et + de 25 ans
        Age = int(input("Rentrer votre âge : "))
        match Age:
            case Age if Age < 18:
                print("Vous avez en dessous de 18 ans.")
                Age = 1
            case Age if Age >= 18 and Age <= 25:
                print("Vous avez entre 18 et 25 ans.")
                Age = 2
            case Age if Age > 25:
                print("Vous avez au dessus de 25 ans")
                Age = 3
        readers.write(str(Age) + " ,")
        Style = int(input(
            "Rentrer 1 si vous aimer la Science-fiction,\nRentrer 2 si vous aimer la Biographie,\nRentrer 3 si vous aimer l'Horreur,\nRentrer 4 si vous aimer la Romance,\nRentrer 5 si vous aimer les Fables,\nRentrer 6 si vous aimer l'Histoire,\nRentrer 7 si vous aimer la Comédie : "))
        readers.write(str(Style) + "\n")


# Connection a son compte
def Connection(file, name):
    with open(file, "r") as readers:
        verification = False
        while verification == False:
            line = readers.readline()
            while line != "" and verification == False:
                if name in line:
                    verification = True
                else:
                    line = readers.readline()
        print("bonjour ", name)



def DisplayUsers(file, file2, name):
    """Seek and show the profil of an user"""
    with open(file, "r") as readers:
        verification = False
        while verification == False:
            line = readers.readline()
            while line != "" and verification == False:
                if name in line:
                    verification = True
                else:
                    line = readers.readline()
    return (print(line))


def DeleteUsers(file, file2, name):
    with open(file, "r") as f:
        with open(file2, "r") as b:
            lines2 = b.readlines()
            lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if name not in line.strip("\n"):
                f.write(line)
    with open(file2, "w") as b:
        for line2 in lines2:
            if name not in line2.strip("\n"):
                b.write(line2)


def users_exist(file, name):
    """"file : reader.txt"""
    with open(file, "r") as f:
        line = f.readline()
        while line != "":
            if name in line:
                return True
            else:
                line = f.readline()
        return False
