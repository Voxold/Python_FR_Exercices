# Nous allons écrire un programme qui affiche la ou les solutions 
# d’une équation du second degré de la forme ax² + bx + c = 0. 

import math

A = int(input("Entrer Valeur de A : "))
B = int(input("Entrer Valeur de B : "))
C = int(input("Entrer Valeur de C : "))


DELTA = (B ** 2) - (4 * A * C)

if DELTA > 0 :
    X1 = (- B - math.sqrt(DELTA)) / 2*A
    X2 = (- B + math.sqrt(DELTA)) / 2*A
    print("Nous avons en cette situation deux solutions pour X : ")
    print("* X1 = ",format(X1,".2f"))
    print("* X2 = ",format(X2,".2f"))

elif DELTA == 0 :
    X = (- B) / (2*A) 
    print("Nous avons en cette situation juse un solution pour X : ")
    print("* X = ",X)
else :
    print("X n'a pas la solution en R!")


    




