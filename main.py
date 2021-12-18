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
                 "for a user;\n 4 to enter the books you have read; \n 5 to add a grade to a book;\n 6 to delete your " \
                 "account;\n 7 to verify that the account exists;\n 8 to quit: \n 9 to log out ;\n 10 to get a book " \
                 "suggestion; \n 11 to see every book available ;\n 12 to look for a particular book ;\n 13 to add a " \
                 "book to our database ;\n 14 to change the title of a book;\n 15 to delete a book from the database " \
                 ";\n 16 to check if you already read a specific book ; \n :"
# menu for the user, making him able to interact with the program
Interface = int(
    input(text_interface))

while Interface > 16 or Interface < 1 or Interface is None:
    Interface = int(
        input(text_interface))

# initialise the pseudo as an empty str
pseudo = ""

while Interface > 0 or Interface < 16 or Interface is not None:

    match Interface:
        case 1:
            Profil("readers.txt", "booksread.txt", Matrix)

        case 2:
            pseudo_temp = str(input("Please enter your pseudo : "))
            pseudo = Connection("readers.txt", pseudo_temp)

        case 3:
            search_ps = str(input("What is the pseudo of the person you are looking for ? : "))
            DisplayUsers("readers.txt", "booksread.txt", search_ps)
        case 4:
            if pseudo == "":
                print("Please, connect to your username")
            else:
                booksread_addBook("readers.txt", "books.txt", "booksread.txt", pseudo)
        case 5:
            update_Matrix("books.txt", "booksread.txt", pseudo)
        case 6:
            answer = str(input("Are you sure you want to delete your profile ? (yes / no) : "))
            while answer != "yes" or answer != "no":
                answer = str(input("Are you sure you want to delete your profile ? (yes / no) : "))
            match answer:
                case "yes":
                    DeleteUsers("readers.txt", "booksread.txt", pseudo)
                case "no":
                    Interface = 100
        case 7:
            print(users_exist("readers.txt", pseudo))
        case 8:
            exit()
        case 9:
            name = ""
            print("successfully logged out")
        case 10:
            init_matrixSimi("readers.txt", "matrix.txt")
            book_suggestion("readers.txt", "matrix_simi.txt", "booksread.txt", "books.txt", pseudo)
        case 11:
            ShowBook("books.txt")
        case 12:
            search = book_exist("books.txt", str(input("What is the book title you are looking for?")))
            print("book is already in the database ." if search == True else "You can add this book .")
            search = ""
        case 13:
            addBook("books.txt", "matrix.txt", str(input("What is the title of the new book ?")))
        case 14:
            changeTitle("books.txt")
        case 15:
            delete_Book("books.txt", "booksread.txt", "matrix.txt")
        case 16:
            if pseudo == "":
                print("Please, connect to your account.")
            else:
                booksread_verify("books.txt", "booksread.txt", pseudo, str(input("What is the title of the book that "
                                                                                 "you need to check ?")))
    # keep user in the  while loop
    #Interface = 100
    wait = input()
    Interface = int(
        input(text_interface))
