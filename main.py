from function import*


create=int(input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
while create > 2 or create < 1:
    create=int(input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
match create:
    case 1:
        create=1
    case 2:
        create=2
if create == 1:
    Profil("readers.txt")

else:
    connection=int(input("voulez vous vous connectez ? si oui tapez 1. Si vous voulez rechercher un utilisateur, tapez 2"))
    while connection<1 or connection>3:
        connection = int(input("voulez vous vous connectez ? si oui tapez 1. Si vous voulez rechercher un utilisateur, tapez 2 ou tapez 3 pour quitter."))
    match connection:
        case 1:
            connection=1
        case 2:
            connection=2
        case 3:
            connection=3
    if connection == 1:
        name = str(input("veuillez rentrer votre Speudo : "))
        Connection("readers.txt",name)
    elif connection == 2 :
        namelook = str(input("veuillez rentrer le Speudo de la personne que vous cherchez : "))
        DisplayUsers("readers.txt", namelook)
    else:
        exit()
