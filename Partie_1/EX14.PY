
# Dans cette vidéo, nous allons écrire le programme suivant :
#Un magasin facture 0,30 dh les dix premières photocopies, 0,25 dh 
#les vingt suivantes et 0,20 dh au-delà. 
#Ecrire un programme qui demande à l’utilisateur le nombre de photocopies effectuées et 
#qui affiche la facture correspondante.

A = int(input("Entrer le nombre Ddes papies : ")) 

if A <= 10 : 
    A = A * 0.30 
    print("Total = ",A,"Dh")

elif 10 < A <= 20 :
    A = A * 0.25 
    print("Total = ",A,"Dh")

else :
    A = A * 0.20
    print("Total = ",A,"Dh")