""" T (entier) exprimé en secondes, et qui le convertit en heures, minutes, 
secondes.
Exemple : T = 56263 seconds =15 heures 37 minutes 43 seconds.
Nous allons écrire un programme qui demande un temps  """

T = int(input("Entrer le temp en second : "))

H = T // 3600
M = (T % 3600)
M2 = M // 60
S = M % 60

print(H,"Heurs",M2,"Minutes",S,"Seconds")

