# Création du Profil
def Profil(file) :
    with open (file,"a") as readers:
        Pseudo=str(input("Rentrer votre Pseudonyme : "))
        readers.write(Pseudo+" ,")
        Genre=0
        while Genre <= 0 or Genre>4:
            Genre = int(input("Si vous êtes un Homme tapez 1 ; \nSi vous êtes une Femme tapez 2 ; \nSi vous souhaitez ne pas rentrer votre genre, tapez 3 : "))
            match Genre:
                case 1:
                    Genre = 1
                case 2 :
                    Genre = 2
                case 3 :
                    Genre = 3
        readers.write(str(Genre)+" ,")
        # age : en dessous de 18 ans , 18-25 ans  et + de 25 ans
        Age = int(input("Rentrer votre âge : "))
        match Age:
            case Age if Age < 18:
                print("Vous avez en dessous de 18 ans.")
                Age = 1
            case Age if Age >= 18 and Age <= 25 :
                print("Vous avez entre 18 et 25 ans.")
                Age= 2
            case Age if Age > 25 :
                print("Vous avez au dessus de 25 ans")
                Age = 3
        readers.write(str(Age)+" ,")
        Style = int(input("Rentrer 1 si vous aimer la Science-fiction,\nRentrer 2 si vous aimer la Biographie,\nRentrer 3 si vous aimer l'Horreur,\nRentrer 4 si vous aimer la Romance,\nRentrer 5 si vous aimer les Fables,\nRentrer 6 si vous aimer l'Histoire,\nRentrer 7 si vous aimer la Comédie : "))
        readers.write(str(Style)+"\n")

#Connection a son compte
def Connection(file,name):
    with open(file,"r") as readers:
        verification=False
        while verification==False:
            line = readers.readline()
            while line != "" and verification== False:
                if name in line:
                    verification=True
                else:
                    line=readers.readline()
        print("bonjour ",name)

#recherche du profil d'un utilisateur
def DisplayUsers(file,file2, name):
    with open(file, "r") as readers:
        verification = False
        while verification == False:
            line = readers.readline()
            while line != "" and verification == False:
                if name in line:
                    verification = True
                else:
                    line = readers.readline()
    return(print(line))

def DeleteUsers(file,name):
    with open(file,"r") as f:
        lines=f.readlines()
    with open(file,"w")as f:
        for line in lines:
            if name not in line.strip("/n"):
                f.write(line)
