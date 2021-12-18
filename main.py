from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *
from matrix_simi_function import*

fm.init_Matrix("Books.txt", "Matrix.txt", "readers.txt")
Matrix = fm.Matrix

# on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
Interface = int(
    input("Would you like to log in? \n 1 to create a profile;\n 2 to continue to the connection;\n 3 to search for a user;\n 4 to enter the books you have read;"
              " \n 5 to add a grade to a book;\n 6 to delete your account;\n7 to verify that the account exists;\n 8 to quit: \n 9 to cancel :")
)

while Interface > 6 or Interface < 1:
    Interface = int(
        input("Would you like to log in? \n 1 to create a profile;\n 2 to continue to the connection;\n 3 to search for a user;\n 4 to enter the books you have read;"
              " \n 5 to add a grade to a book;\n 6 to delete your account;\n7 to verify that the account exists;\n 8 to quit: \n 9 to cancel :")
    )
# initialise the pseudo as an empty str
pseudo = ""

while Interface > 0 or Interface < 10:

    match Interface:
        case 1:
            Profil("readers.txt", "booksread.txt", Matrix)
            print(Matrix)
            fm.save_matrix("Matrix.txt", Matrix)
        case 2:
            pseudo = str(input("Please enter your pseudo : "))
            pseudo = Connection("readers.txt", name)

        case 3:
            namelook = str(input("veuillez rentrer le pseudo de la personne que vous cherchez : "))
            DisplayUsers("readers.txt", "booksread.txt", namelook)
        case 4:
            booksread_addBook("Books.txt", "booksread.txt", name)
        case 5:
            update_Matrix("Books.txt", "booksread.txt", name)
        case 6:
            answer = str(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
            while answer != "yes" or answer != "no":
                answer = str(input("etes vous sur de supprimer votre profil  ? (yes / no) : "))
            match answer:
                case "yes":
                    DeleteUsers("readers.txt", "booksread.txt", name)
                    print("your profile has been delete")
                case "no":
                    Interface = 9
                    # exit("Action cancelled")
        case 7:
            print(users_exist("readers.txt", name))
        case 8:
            exit()
        case 9:
            name = ""
        case 10:
            init_matrixSimi("readers.txt", "Matrix.txt")
            book_suggestion("readers.txt", "Matrice_similarité.txt", "booksread.txt", "Books.txt", pseudo)

    # stuck user in the  while loop
    Interface = 100
