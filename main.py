from functionUsers import *
from function import *
import FunctionMatrix as fm


fm.init_Matrix("Books.txt", "Matrix.txt", "readers.txt") # "Matrix =" l'init?
Matrix = fm.Matrix
print("m ", Matrix)
# on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
Interface = int(
    input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour saisir les livres que vous avez lus;"
          "\n 5 pour ajouter une note à un livre;\n 6 pour supprimer votre compte;\n 7 pour vérifier que le compte existe;\n 8 pour quitter : ")
)

while Interface > 6 or Interface < 1:
    Interface = int(
        input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour saisir les livres que vous avez lus;"
              "\n 5 pour ajouter une note à un livre;\n 6 pour supprimer votre compte;\n 7 pour vérifier que le compte existe;\n 8 pour quitter : ")
    )

match Interface:
    case 1:
        Profil("readers.txt", "booksread.txt", Matrix)
        print(Matrix)
        fm.save_matrix("Matrix.txt", Matrix)
    case 2:
        name = str(input("veuillez rentrer votre Speudo : "))
        Connection("readers.txt", name)


    case 3:
        namelook = str(input("veuillez rentrer le pseudo de la personne que vous cherchez : "))
        DisplayUsers("readers.txt", "booksread.txt", namelook)
    case 4:
        name = str(input("veuillez rentrer votre Speudo : "))
        booksread_addBook("Books.txt", "booksread.txt", name)
    case 5:
        name = str(input("veuillez rentrer votre Speudo : "))
        update_Matrix("Books.txt", "booksread.txt", name)
    case 6:
        name = str(input("veuillez rentrer votre Speudo : "))
        answer = int(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
        while answer != "yes" or answer != "no":
            answer = str(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
        match answer:
            case "yes":
                DeleteUsers("readers.txt", "booksread.txt", name)
                print("your profile has been delete")
            case "no":
                exit("Action cancelled")
    case 7:
        name = str(input("veuillez rentrer le Speudo que vous recherchez: "))
        print(users_exist("readers.txt", name))
        exit()
    case 8:
        exit()



# delete_Book("Books.txt","booksread.txt")hh
#booksread_addBook("")
# init_Matrix("Books.txt","readers.txt")
