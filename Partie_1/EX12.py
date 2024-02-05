# Nous allons écrire un programme qui retourne si deux nombres
# entiers donnés sont de même signe ou non.

A = int(input("Entrer le premiere nombre : ")) 
B = int(input("Entrer le deuxieme nombre : ")) 

if A * B > 0 : 
    print("Les deux nombres ont meme signes!")
else :
    print("Les deux nombres n'ont pas meme signes!")
