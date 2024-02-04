
# Écrire un programme Python qui demande l'âge d'un enfant et permet 
#d'informer de sa catégorie sachant que les catégories sont les suivantes: 
#"poussin de 6 a 7 ans"   
#"pupille de 8 a 9 ans "   
#"minime de 10 a 11 ans "  
#" cadet après 12 ans ". 

A = int (input ("Veuillez entrer age d'enfant : "))

if 6 <= A <= 7 :
    print("Pupille")

elif 8 <= A <= 9 :
    print("Poussin")

elif 10 <= A <= 11 :
    print("Minime")

elif A < 6 :
    print("INCORRECT")

else :
    print("Cadet")
