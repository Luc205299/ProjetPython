from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *
from matrix_simi_function import *

# init the grade matrix
fm.init_Matrix("books.txt", "matrix.txt")
Matrix = fm.Matrix
text_interface = "What would you like to do ? \n 1 to create a profile;\n 2 to continue to the connection;\n 3 to " \
                 "search " \
                 "for a user;\n 4 if you are an administrator\n :"

text_Userinterface = "What would you like to do ? \n 1 to enter the books you have read; \n 2 to rate a book;\n 3 to delete your " \
                     "account;\n 4 to get a book " \
                     "suggestion; \n 5 to see every book available ;\n 6 to look for a specific book ;\n 7 to add a " \
                     "book to our database ;\n 8 to check if you already read a specific book ; \n 9 to log out :"
text_Admininterface = "What would you like to do ? \n 1 to verify that the account exists;\n 2 to change the title of a book;\n 3 to delete a book from the database " \
                      ";\n 4 to quit ; \n :"
# menu for the user, making him able to interact with the program
Interface = int(
    input(text_interface))

while Interface < 0 or Interface > 4 or Interface is None:
    Interface = int(
        input(text_interface))

# initialise the pseudo as an empty str
pseudo = ""
while Interface > 1 or Interface < 4:
    match Interface:
        case 1:
            Profil("readers.txt", "booksread.txt", Matrix)

        case 2:
            pseudo_temp = str(input("Please enter your pseudo : "))
            pseudo = Connection("readers.txt", pseudo_temp)
            if pseudo != "":
                user_interface = (int(
                    input(text_Userinterface)))
            while user_interface > 9 or user_interface < 1:
                user_interface = int(
                    input(text_Userinterface))

            while 9 > user_interface > 1:
                match user_interface:

                    case 1:
                        booksread_addBook("readers.txt", "books.txt", "booksread.txt", pseudo)
                    case 2:
                        update_Matrix("books.txt", "booksread.txt", pseudo)
                    case 3:
                        answer = str(input("Are you sure you want to delete your profile ? (yes / no) : "))
                        while answer != "yes" or answer != "no":
                            answer = str(input("Are you sure you want to delete your profile ? (yes / no) : "))
                        match answer:
                            case "yes":
                                DeleteUsers("readers.txt", "booksread.txt", pseudo)
                            case "no":
                                user_interface = 100
                    case 4:
                        init_matrixSimi("matrix_simi.txt", "matrix.txt")
                        book_suggestion("readers.txt", "matrix_simi.txt", "booksread.txt", "books.txt", pseudo)
                    case 5:
                        ShowBook("books.txt")
                    case 6:
                        search = book_exist("books.txt", str(input("What is the book title you are looking for?")))
                        print("book is already in the database ." if search == True else "You can add this book .")
                        search = ""
                    case 7:
                        addBook("books.txt", "matrix.txt", str(input("What is the title of the new book ?")))

                    case 8:
                        if pseudo == "":
                            print("Please, connect to your account.")
                        else:
                            booksread_verify("books.txt", "booksread.txt", pseudo,
                                             str(input("What is the title of the book that "
                                                       "you need to check ?")))
                    case 9:
                        # log out
                        name = ""
                        print("successfully logged out")
                        user_interface = 11

                #wait = input()

        case 3:
            search_ps = str(input("What is the pseudo of the person you are looking for ? : "))
            DisplayUsers("readers.txt", "booksread.txt", search_ps)

        case 4:
            admininterface = (int(
                input(text_Admininterface)))
            while 1 > admininterface or admininterface > 4:
                admininterface = (int(
                    input(text_Admininterface)))
            match admininterface:
                case 1:
                    user = str(input("Enter the username of the user you looking for : "))
                    print(users_exist("readers.txt", user))
                case 4:
                    exit()
                case 2:
                    changeTitle("books.txt")
                case 3:
                    delete_Book("books.txt", "booksread.txt", "matrix.txt")
            wait = input()
    # keep user in the  while loop
    wait = input()
    Interface = int(
        input(text_interface))
