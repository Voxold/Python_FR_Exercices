# Écrire un programme Python permettant d’afficher le mois en lettre 
#selon le numéro saisi au clavier.  
#(  Si l’utilisateur tape 1 le programme affiche janvier,  
#si 2  affiche  février , si 3 affiche mars... ).  

A = int (input ("Veuillez entrer le nombre : "))

# j'ai utilise ici les jours de semain :

if A == 1 :
    print("Lundi")
elif A == 2 :
    print("Mardi")
elif A == 3 :
    print("Mercredi")
elif A == 4 :
    print("Jeudi")
elif A == 5 :
    print("Vendredi")
elif A == 6 :
    print("Samedi")
elif A == 7 :
    print("Dimache")
else :
    print("ERROR")
