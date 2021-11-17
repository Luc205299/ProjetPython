from functionUsers import*

#on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
Interface=int(input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour quitter : "))
while Interface > 4 or Interface < 1:
    Interface=int(input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
match Interface:
    case 1:
        Interface=1
    case 2:
        Interface=2
    case 3:
        Interface=3
    case 4:
        Interface=4
if Interface == 1:
    Profil("readers.txt")
elif Interface ==2:
    name = str(input("veuillez rentrer votre Speudo : "))
    Connection("readers.txt", name)

elif Interface == 3:
    namelook = str(input("veuillez rentrer le Speudo de la personne que vous cherchez : "))
    DisplayUsers("readers.txt", namelook)
else:
    exit()
