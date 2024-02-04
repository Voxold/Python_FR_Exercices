
# Dans cette vidéo, nous allons écrire un programme qui demande l’âge et le sexe 
# d’un habitant et affiche si celui-ci est imposable. 

# Hommes plus 20 ans ==> paient l'impot 
# femmes entre 18 et 35ans ==> paient l'impot 
# rest non paient impot

Sexe = input("Entre le sexe d'habite : ")
Age = int(input("Entre l'age' d'habite : "))

if Sexe == "Homme" and Age >= 20 :
    print("Ce homme il est paye d'impot!")
elif Sexe == "Femme" and 18 <= Age <= 35 :
    print("Cette femme elle est paye d'impot!")
elif  Sexe == "Homme" and Age < 20 : 
    print("Ce person pas obliger pour paye l'impot!")
elif  Sexe == "Femme" and Age < 18 or Age > 35 :
    print("Ce person pas obliger pour paye l'impot!")
else :
    print("EROOR")

