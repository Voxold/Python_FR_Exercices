
# Dans cette vidéo, nous allons écrire un programme qui demande à l’utilisateur 
#de saisir un nombre puis qui en fonction du nombre saisi :
#– 6 : affiche « le personnage va à droite ».
#– 4 : affiche « le personnage va à gauche ».
#– 8 : affiche « le personnage va en haut ».
#– 2 : affiche « le personnage va en bas ».
#– dans le cas d’un autre caractère, affiche : « erreur de saisie,
# le personnage ne bouge pas ».

N = int(input("Entrer le nombre pour donner un mission : "))

if N == 6 :
    print("le personnage va à droite")
elif N == 4 :
    print("le personnage va à gauche")
elif N == 8 :
    print("le personnage va en haut")
elif N == 2 :
    print("le personnage va en bas")
else :
    print("Erreur de saisie, Le personnage ne bouge pas!")