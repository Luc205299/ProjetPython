
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

# age : en dessous de 18 ans , 18-25 ans  et + de 25 ans
Age = int(input("Rentrer votre âge : "))
match Age:
    case mineur if Age < 18:
        print("Vous avez en dessous de 18 ans.")
    case entre2 if Age >= 18 and Age <= 25 :
        print("Vous avez entre 18 et 25 ans.")
    case mineur if Age > 25 :
        print("Vous avez au dessus de 25 ans")
