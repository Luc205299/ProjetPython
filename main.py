from functionUsers import*
from function import*
from FunctionMatrix import*

# #on demande si il veut se creer un profil, se connecter, rechercher un utilisateur ou quitter
# Interface=int(input("voulez vous vous connectez ? \n 1 pour créer un profil;\n 2 pour poursuivre a la connection;\n 3 pour rechercher un utilisateur;\n 4 pour quitter : "))
# while Interface > 5 or Interface < 1:
#     Interface=int(input("voulez vous vous connectez ? ( 1 pour créer un profil et 2 pour poursuivre a la connection : "))
# match Interface:
#     case 1:
#         Profil("readers.txt")
#     case 2:
#         name = str(input("veuillez rentrer votre Speudo : "))
#         Connection("readers.txt", name)
#         answer = str(input("etes vous sur de supprimer votre profil  ? : "))
#         while answer > 2 or answer < 1:
#             answer = str(input("etes vous sur de supprimer votre profil  ? : "))
#         match answer:
#             case 1:
#                 exit()
#             case 2:
#                 DeleteUsers("readers.txt", name)
#
#
#     case 3:
#         namelook = str(input("veuillez rentrer le Speudo de la personne que vous cherchez : "))
#         DisplayUsers("readers.txt","booksread.txt", namelook)
#     case 4:
#         IniMatrix("readers.txt", "Books.txt")
#         exit()
#delete_Book("Books.txt","booksread.txt")
init_Matrix("Books.txt","readers.txt")