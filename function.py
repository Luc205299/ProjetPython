def Profil() :

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
        case Age if Age < 18:
            print("Vous avez en dessous de 18 ans.")
        case Age if Age >= 18 and Age <= 25 :
            print("Vous avez entre 18 et 25 ans.")
        case Age if Age > 25 :
            print("Vous avez au dessus de 25 ans")

    Style = int(input("Rentrer 1 si vous aimer la Science-fiction,\nRentrer 2 si vous aimer la Biographie,\nRentrer 3 si vous aimer l'Horreur,\nRentrer 4 si vous aimer la Romance,\nRentrer 5 si vous aimer les Fables,\nRentrer 6 si vous aimer l'Histoire,\nRentrer 7 si vous aimer la Comédie : "))
