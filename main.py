from functionUsers import *
from function import *
from FunctionMatrix import *
from Matrice_simi import *

init_Matrix("Books.txt", "readers.txt")

# # #on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
# Interface = int(
#     input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour quitter : "))
# while Interface > 6 or Interface < 1:
#     Interface = int(
#         input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
# match Interface:
#     case 1:
#         Profil("readers.txt", "booksread.txt")
#         print(Matrix)
#     case 2:
#         name = str(input("veuillez rentrer votre Speudo : "))
#         Connection("readers.txt", name)
#         answer = int(input("etes vous sur de supprimer votre profil  ? (1 / 2) : "))
#         while answer > 2 or answer < 1:
#             answer = str(input("etes vous sur de supprimer votre profil  ? : "))
#         match answer:
#             case 2:
#                 print(verification_users("readers.txt", name))
#                 exit()
#             case 1:
#                 DeleteUsers("readers.txt","booksread.txt", name)
#             case _:
#                 print("entrez oui pour suprrimer, non pour ne pas supprimer")
#
#     case 3:
#         namelook = str(input("veuillez rentrer le Speudo de la personne que vous cherchez : "))
#         DisplayUsers("readers.txt", "booksread.txt", namelook)
#     case 4:
#         exit()
#     case 5:
#         booksread_addBook("Books.txt", "booksread.txt", "skusku")
#     case 6:
#         update_Matrix("Books.txt", "booksread.txt", "skusku ")
#     case _:
#         print("entrez une commande valide...")

# delete_Book("Books.txt","booksread.txt")hh
#booksread_addBook("")
# init_Matrix("Books.txt","readers.txt")
save_matrix("Matrix.txt", Matrix)
init_matrixSimi("Matrice_similarité.txt")
