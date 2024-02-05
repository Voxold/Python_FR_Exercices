""" 
Nous allons écrire un programme qui calcule et affiche 
la distance entre deux points A et B du plan dont les coordonnées (XA , YA) 
et (XB , YB) sont entrées au clavier comme entiers. 
on utilise distance AB = racing (xb-xa)2 + (yb-ya)2
on utilise aussi math.sqrt() fonction pour racing care 
"""


import math

print("Voici le programme aue peut utilise pour calcule la distance entre A et B.")

XA = int(input("Entre point de Xa : "))
YA = int(input("Entre point de Ya : "))
XB = int(input("Entre point de Xb : "))
YB = int(input("Entre point de Yb : "))

AB = (( XB - XA )**2) + (( YB - YA )**2)
AB = math.sqrt(AB)

print("La distance entre A et B est : AB = ",format(AB,".2f"))