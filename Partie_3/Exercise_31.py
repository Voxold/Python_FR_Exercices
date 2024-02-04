# Écrire un programme Python permettant de  calculer la somme   
#S=1+2+3+...+ N,  où N saisi par l’utilisateur.  
#Utilisant la  boucle while.  

N = int(input("Veuillez entrer un nombre : "))

S = 0 
i = 1

while i <= N :
    S = S + i
    i = i + 1

print("La somme de N est : ",S)