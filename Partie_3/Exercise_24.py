# fornction 2
# ax + bx + c = 0

import math

A = int(input("Entrer valeur de A : "))
B = int(input("Entrer valeur de B : "))
C = int(input("Entrer valeur de C : "))

print("")
print("Donc pour la solution de fonction : ",A,"X2 + ",B,"X + ",C," = 0 :" )
print("")

DELTA = (-B**2) + (4 * A * C)
if DELTA > 0 :
    print("La fonction accepte 2 solutions : ") 
    print("")
    DT = math.sqrt(DELTA)
    X1 = ( - B - DT ) / 2*A
    X2 = ( - B + DT ) / 2*A
    print("X1 = ",X1)
    print("X2 = ",X2)

elif DELTA == 0 :
    X = -B / 2*A
    print("La fonction accepte 1 seul solution : ") 
    print("")
    print("X = ",X)

else :
    print("La fonction n'ai pas la solution!")
