from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *
from matrix_simi_function import*


fm.init_Matrix("books.txt", "matrix.txt", "readers.txt")
Matrix = fm.Matrix

# secured input
Interface: int = 0

while Interface == "" or type(Interface) != int() or Interface > 0 or Interface < 10:
    Interface = int(Interface)
    # initialise the pseudo as an empty str
    pseudo = ""

    match Interface:
        case 1:
            Profil("readers.txt", "booksread.txt", Matrix)
            print(Matrix)
            fm.save_matrix("matrix.txt", Matrix)
        case 2:
            pseudo = str(input("veuillez rentrer votre Speudo : "))
            pseudo = Connection("readers.txt")

        case 3:
            namelook = str(input("veuillez rentrer le pseudo de la personne que vous cherchez : "))
            DisplayUsers("readers.txt", "booksread.txt", namelook)
        case 4:
            booksread_addBook("books.txt", "booksread.txt", pseudo)
        case 5:
            update_Matrix("books.txt", "booksread.txt", pseudo)
        case 6:
            answer = str(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
            while answer != "yes" or answer != "no":
                answer = str(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
            match answer:
                case "yes":
                    DeleteUsers("readers.txt", "booksread.txt", pseudo)
                    print("your profile has been delete")
                case "no":
                    Interface = 9
        case 7:
            print(users_exist("readers.txt", pseudo))
        case 8:
            exit()
        case 9:
            name = ""
        case 10:
            init_matrixSimi("readers.txt", "matrix.txt")
            book_suggestion("readers.txt", "matrix_simi.txt", "booksread.txt", "books.txt", pseudo)

    # keep user in the  while loop
    Interface = 100
    Interface = int(
        input("Que voulez vous faire ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour "
              "rechercher un utilisateur;\n 4 pour saisir les livres que vous avez lus; "
              "\n 5 pour ajouter une note à un livre;\n 6 pour supprimer votre compte;\n 7 pour vérifier que le "
              "compte existe;\n 8 pour quitter : \n 9 pour déco ;\n 10 pour recommander un livre"))