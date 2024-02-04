
# Écrire un programme Python qui permet de calculer la somme    
#S=1+2+3+4+….+ N. où N saisi au clavier par l'utilisateur.
#Utilisant la boucle for. 

N = int(input("Veuillez entrer um nombre :"))

S = 0
for i in range(1,N+1) :
    S = S + i

print("La somme entre nombres 1 et ",N," est = ",S)
