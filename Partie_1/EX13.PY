
# Dans cette vidéo, nous allons écrire un programme qui échange les contenus 
# de deux données numérique si elles sont de même signe, sinon il met la somme 
# des deux dans la première donnée et leur produit dans la seconde.

A = int(input("Entrer le premiere nombre : ")) 
B = int(input("Entrer le deuxieme nombre : ")) 

if A * B > 0 : 
    C = A
    A = B
    B = C
    print("La valeur de A est : ",A)
    print("La valeur de B est : ",B)
else :
    S = A + B
    P = A * B
    print("La somme des deux nombres est : A + B = ",S)
    print("Le produit des deux nombres est : A x B = ",P)