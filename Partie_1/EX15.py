# Nous allons écrire un programme qui demande l’âge d’un enfant 
# l’utilisateur. Ensuite, il l’informe de sa catégorie : "Poussin" de 6 à 7 ans, 
# "Pupille" de 8 à 9 ans, "Minime" de 10 à 11 ans, "Cadet" après 12 ans.
# 6 <= age <= 7  ==> Poussin 
# 8 <= age <= 9  ==> Pupille
# 10 <= age <= 11  ==>Minime
# 12 <= age   ==> Cadet

Age = int(input("Entrer l'age d'enfent : "))

if 6 <= Age <= 7 :
    print("Poussin")

elif 8 <= Age <= 9 :
    print("Pupille")

elif 10 <= Age <= 11 :
    print("Minime")

elif Age >= 12 :
    print("Cadet")

else : 
    print("ERROR")