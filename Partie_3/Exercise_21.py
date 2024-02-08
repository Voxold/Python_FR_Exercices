# Écrire un programme Python qui permet d'afficher la table de 
# multiplication d’un entier saisie par l’utilisateur, 
# Utilisant la boucle for.  

N = int(input("Veuillez entrer un nombre : "))

for i in range(0,11) :
    S = N * i
    print(i," x ",N," = ",S)