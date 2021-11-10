
#Création du Profil

Pseudo=str(input("Rentrer votre Speudonyme : "))

Genre = int(input("Si vous êtes un Homme tapez 1 ; \nSi vous êtes une Femme tapez 2 ; \nSi vous souhaitez ne pas rentrer votre genre, tapez 3 : "))

match Genre:
    case 1:
        Genre = "Homme"
    case 2 :
        Genre = "Femme"
    case 3 :
        Genre = "Non Précisé"

Age = int(input("Rentrer votre âge : "))