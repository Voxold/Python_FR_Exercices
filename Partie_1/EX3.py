
# Dans cette vidéo, nous allons écrire un programme qui demande à l'utilisateur 
# de taper la largeur et la longueur d'un rectangle et qui en affiche le périmètre
# et la surface.

A = int(input("Entrer LARGEUR de rectangle :"))
B = int(input("Entrer LANGEUR de rectangle :"))

P = 2 * ( A + B )
S  = A * B

print("le périmètre est : P = ",P)
print("la surface est : S = ",S)