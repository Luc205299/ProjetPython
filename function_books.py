""" Book recommandation project, programming in python

    Sylvan Buhard
    Lucas Barthelemy
    function_books.py: gathers each function linked to the library and books management,
     and associated features."""

# importations needed
from function_matrix import *
import function_matrix as fm
from function_books import *
from math import *
from function_users import *


def is_empty(file:str) -> bool:
    """return true if a file is empty
    file : the file to check
    :return bool
    """
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        content = f.readlines()
        # if file is empty, return True
        if len(content) == 0:
            return True
    # else return false
    return False


def ShowBook(file: str):
    """function to open and read the Books file and print what's inside
    file: the file un want to read (.txt)
    listing: list of books to show, and not the others
    :return nothing, it us a display function"""
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
    # print every book in the folder, with it number
    print("Here is the book database :\n")
    for count, content in enumerate(content):
        print(count, ":", content)


def book_exist(file1, name) -> tuple:
    """function to search if a book exist and return it number if it is true
    file: books (.txt)
    name: name of the book
    :return tuple ( bool, int ) """
    # open file in read mode
    with open(file1, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for line in content:
            line2 = line.strip('\n')
            if line2 == name:
                return True, content.index(line)
    return False, -1


def addBook(file: str, file2: str, name: str = None):
    """function to add a book at the end of the file
    file: book (.txt)
    file2: matrix.txt
    name: the name of the book you want to append
    :return nothing, write in the file"""
    if name is None:
        name = str(input("What is the title of the book : "))
    exist = book_exist(file, name)

    if not exist:
        j = open(file, "a", encoding='utf-8')
        j.write('\n' + name)
        j.close()
    else:
        return print("Book already exist, you can rate it.")
    # append it at the end of matrix
    matrix = fm.import_matrix(file2)
    matrix[0].append(name)
    for i in range(1, len(matrix)):
        matrix[i].append('0')
    fm.save_matrix(file2, matrix)
    print("Database has been updated.")


def changeTitle(file: str):
    """function to modify an existing book in file
    file: the file un want to read (.txt)
    name: the name of the book you want to modify
    :return nothing, this is an update function"""

    name = str(input("What is the title of the book you want to modify ? :"))
    index_src = None
    # list of file data
    data_list = []
    # open file in read mode
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for ligne in content:
            # print(ligne," et ", name)
            data_list.append(ligne)
            if str(ligne) == name:
                index_src = content.index(ligne)
                # print(index_src, "index src")

    if index_src is None:
        return print("This book isn't in the database.")

    elif type(index_src) == int:
        # 2nd open of the file to modify data
        new_title = str(input("Enter the new title of the book ? :"))
        data_list[index_src] = new_title
        with open(file, "w", encoding='utf-8') as f:
            # write new data open file
            for elt in data_list:
                f.write(elt)


def delete_Book(file: str, file2: str, file3: str):
    """ delete an existing book from the repository/library of file in argument
    file : books.txt
    file2: booksread
    file3 : matrix.txt
    :return nothing, this is an update function"""
    # if the book exist
    matrix = fm.import_matrix(file3)
    name = str(input("Enter the title of the book to delete :"))
    position = book_exist(file, name)[1]+1
    if position == 0:
        return print(f"{name} isn't in the database.")
    # list of file data
    data_list = []
    # delete occurrences in each line
    for i in range(1, len(matrix)):
        matrix[i].pop(position)
    # delete the title on first line
    test = matrix[0].pop(position)
    fm.save_matrix(file3, matrix)

    # delete occurrences in booksread
    with open(file2, "r", encoding='utf-8') as f2:
        # read open file to search the book occurrences
        content = f2.readlines()
        for elt in content:
            tmp = elt.strip(',\n').strip(' ').split(',')
            for elt2 in tmp[1:]:
                if int(elt2)+1 > position:
                    # rewrite every value of books minus one, to fill the hole let by the deleted book
                    tmp[tmp.index(elt2)] = str(int(elt2) - 1)
                elif int(elt2)+1 == position:
                    tmp.pop(tmp.index(elt2))
            # rewrite every element in the line separated by a coma
            data_list.append(tmp)

    # rewrite data in the file without the deleted one
    with open(file2, "w", encoding='utf-8') as f:
        # write new data open file
        for elt in data_list:
            for elt2 in elt:
                if elt.index(elt2) == 0:
                    f.write(elt2)
                else:
                    f.write("," + elt2)
            f.write('\n')

    # delete in books.txt
    data_list = []
    with open(file, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        for line in content:
            l2 = line.strip('\n')
            if l2 != name:
                data_list.append(l2)
            else:
                index_src = content.index(line)
                #rewrite data with correct list of read books
    with open(file, "w", encoding='utf-8') as f:
        # write new data in opened file
        for elt in data_list:
            f.write(elt + '\n')
    print(f"{name} has been deleted.")


def booksread_verify(file1, file2, reader, title) -> tuple:
    """verify is a book as been read by the reader
       file1: books
       file2: booksread
       reader, the currently logged user
       :return tuple( bool, int ) """
    # check if the title exist
    test = book_exist(file1, title)
    if test[0] is False:
        return f": {title} doesn't exist, add it before."
    else:
        position = test[1]
    # open file in read mode
    with open(file2, "r", encoding='utf-8') as f:
        # read open file
        content = f.readlines()
        # check for the reader line
        for line in content:
            l2 = line.strip(',\n').strip(' ').split(',')
            # verify if the book is already written
            if l2[0].strip(' ') == reader:
                # if found, stop the process with return function, from the second elt in list
                for elt in l2[1:]:
                    if int(elt) == int(position):
                        return True, position
        return False, 0


def booksread_addBook(file, file1, file2, reader, title=None):
    """update the folder with each reader and the books he has read
    file: readers
    file1: books
    file2: booksread
    reader, the currently logged user
    title: the title of the book
    :return nothing, this is an update function"""
    # verify is the user is connected
    if not users_exist(file, reader):
        return print("Please connect with a valid username")
    # title of the book for identification
    if title is None:
        title = str(input("Which book did you read ? :"))
    test = book_exist(file1, title)
    if test[0] is False:
        return f"{title}, doesn't exist, add it before."
    else:
        position = test[1]
    verification = False
    # copy the data in the file before the changes
    data_list = []
    # test if the reader has already added the book in the booksread file
    test_presence = booksread_verify(file1, file2, reader, title)
    if test_presence[0] is True:
        return print("This book has already been added.")
    else:
        # open file in read mode
        with open(file2, "r", encoding='utf-8') as f:
            # read open file
            content = f.readlines()
            for line in content:
                l2 = line.strip('\n').split(' ,')
                # search for the reader line
                if l2[0].strip(' ') == reader:
                    verification = True
                    # if not written, add position related to the book at the end of the line, and separated by a coma
                    l3 = line.strip(',\n')
                    l3 = l3 + "," + str(position) + '\n'
                    data_list.append(l3)
                else:
                    data_list.append(line)

    # 2nd open of the file to rewrite data with correct list of read books
    with open(file2, "w", encoding='utf-8') as f:
        # write new data in opened file
        for elt in data_list:
            f.write(elt)
    if verification is False:
        return print("Impossible to find your profile.")
    else:
        print("Your list has been updated.")
