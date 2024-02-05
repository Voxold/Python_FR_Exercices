# Nous allons écrire un programme qui calcule le prix 
#TTC d’un produit connaissant son prix hors taxe et sa catégorie.

P = int(input("Entrer le prix de produit : "))
Cat = input("Entrer le categorie de produit : ")

A = P + (P * 0.07)
B = P + (P * 0.2)
C = P + (P * 0.25)


if Cat == "A" :
    print("Prix Total est : P = ",format(A,".2F"),"Dh")
elif Cat == "B" :
    print("Prix Total est : P = ",format(B,".2F"),"Dh")
elif Cat == "C" :
    print("Prix Total est : P = ",format(C,".2F"),"Dh")
else : 
    print("La Categorie n'existe pas!")