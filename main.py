from functionUsers import*

#on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
create=int(input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour quitter : "))
while create > 4 or create < 1:
    create=int(input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
match create:
    case 1:
        create=1
    case 2:
        create=2
    case 3:
        create=3
    case 4:
        create=4
if create == 1:
    Profil("readers.txt")
elif create ==2:
    name = str(input("veuillez rentrer votre Speudo : "))
    Connection("readers.txt", name)
elif create == 3:
    namelook = str(input("veuillez rentrer le Speudo de la personne que vous cherchez : "))
    DisplayUsers("readers.txt", namelook)
else:
    exit()
