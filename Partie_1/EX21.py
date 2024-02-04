
# Dans cette vidéo, nous allons écrire un programme qui demande deux nombres entiers 
#et l’une des opérateurs suivant : + , - , * , / puis effectue l’opération correspond
#et affiche le résultat de cette opération.

A = int(input("Entrer le premiere nombre : "))
C = input("Entrer le chiffre de calcul : ")
B = int(input("Entrer le deuxieme nombre : "))


S = A + B
D = A - B
Div = A / B
P = A * B

if C == "+" :
    print("A + B = ",format(S,".2f"))
elif C == "*" :
    print("A + B = ",format(P,".2f"))
elif C == "-" :
    print("A + B = ",format(D,".2f"))
elif C == "/" :
    print("A / B = ",format(Div,".2f"))
else :
    print("Error")


