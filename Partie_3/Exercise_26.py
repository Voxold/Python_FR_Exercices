# Le centre de photocopie facture 0,25 DH  pour les 10 premières 
# photocopies, 0,20 DH les vingt suivantes et 0,10 DH pour plus de vingt. 
# Ecrire un programme Python qui demande à l’utilisateur de saisir le nombre 
# de photocopies effectuées et qui affiche la facture correspondante. 

A = int (input ("Veuillez entrer total des pages : "))

if A <= 10 :
    B = A * 0.25
    print("Total de photocopie est : ",B," Dh")

elif 10 < A <= 20 :
    B = A * 0.20
    print("Total de photocopie est : ",B," Dh")

else :
    B = A * 0.10
    print("Total de photocopie est : ",B," Dh")

print("Merci pour votre visit!")
print("")