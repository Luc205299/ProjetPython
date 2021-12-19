from function_matrix import *
import function_matrix as fm


def Profil(file, file2, Matrix):
    """Function to create user profile with name, gender, age, and style liked by the user
    file : readers.txt
    file2 : booksread.txt
    Matrix : Matrix
    """
    with open(file, "a") as readers:
        with open(file2, "a") as br:
            # ask the username and add it to the file "readers.txt" and "booksread.txt"
            Pseudo = str(input("Enter your name : "))
            while users_exist(file, Pseudo) == True or username_ascii(Pseudo) == False:
                Pseudo = str(input("Enter your name (only letter and capital letter): "))
            readers.write(Pseudo + ",")
            br.write(Pseudo + " ,\n")
            temp_list = [i - i for i in range(len(Matrix[0]))] #-1
            temp_list[0] = Pseudo
            Matrix.append(temp_list)
            fm.save_matrix("matrix.txt", Matrix)
        Gender = 0
        while Gender <= 0 or Gender > 4:
            Gender = int(input(
                "If you are a Man type 1 ;\nIf you are a Woman type 2 ;\nIf you do not wish to enter your Gender, type 3 : "))
        readers.write(str(Gender) + ",")
        # age : below 18 years old , 18-25 years old  and more than 25 years old
        Age = int(input("Enter your age : "))
        while Age > 130 or Age < 0:
            Age = int(input("Enter your age : "))
        match Age:
            case Age if Age < 18:
                print("You are under 18 years old.")
                Age = 1
            case Age if Age >= 18 and Age <= 25:
                print("You are between 18 and 25 years old.")
                Age = 2
            case Age if Age > 25:
                print("You are over 25 years old")
                Age = 3
        readers.write(str(Age) + ",")
        Style = int(input(
            "Enter 1 if you like Science Fiction,\nEnter 2 if you like Biography,\nEnter 3 if you like Horror,\nEnter 4 if you like Romance,\nEnter 5 if you like Fables,\nEnter 6 if you like History,\nEnter 7 if you like Comedy:")
        )
        while Style > 7 or Style < 0:
            Style = int(input(
                "Enter 1 if you like Science Fiction,\nEnter 2 if you like Biography,\nEnter 3 if you like Horror,\nEnter 4 if you like Romance,\nEnter 5 if you like Fables,\nEnter 6 if you like History,\nEnter 7 if you like Comedy:")
            )
        readers.write(str(Style) + "\n")


# Connection to the user's account
def Connection(file, name):
    """ enable the user to connect to his account
    file : "readers.txt"
    name : name of the user
    """
    with open(file, "r") as readers:
        line = readers.readlines()
        for elt in line:
            if name == elt.split(',')[0]:
                print("Hello ", name)
                return elt.split(',')[0]
        print(f"No username {name} found, please, create one.")
        return None


def DisplayUsers(file, file2, name):
    """Seek and show the profil of an user
    file : readers.txt
    file 2 : booksred.txt
    name : name of the user
    """
    with open(file, "r") as readers:
        with open(file2, "r") as br:
            verification = False
            verification2 = False
            while verification is False:
                line = readers.readline()

                while line != "" and verification == False:
                    if name in line:
                        verification = True
                    else:
                        line = readers.readline()
                return print("user not found")
            while verification2 == False:
                line2 = br.readline()
                while line2 != "" and verification2 == False:
                    if name in line2:
                        verification2 = True
                    else:
                        line2 = br.readline()
            return print("user not found")
    return print("readers : ", line, "booksread : ", line2)


def DeleteUsers(file, file2, name):
    """ delete the user in readers.txt and booksread.txt

    :param file: readers.txt
    :param file2: booksread.txt
    :param name: name of the user
    :return: nothing
    """
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
    print("Your profile has been deleted.")


def users_exist(file, name):
    """
    Seek if the user exist in the file readers.txt
    :param file: readers.txt
    :param name: name of the user
    :return: True if the username exist and False if he doesn't
    """
    with open(file, "r") as f:
        line = f.readline()

        while line != "":
            if name in line:
                return True
            else:
                line = f.readline()
        return False


def username_ascii(name):
    """
    allows to secure the entry of the user name
    :param name: username of the user
    :return: True if the username is correct and False if he doesn't correct
    """
    for i in name:
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            verif = True
        else:
            return False
    return verif
