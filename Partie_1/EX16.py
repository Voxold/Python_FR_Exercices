# Nous allons écrire un programme permettant de saisir trois notes
# (sur 20) d'un étudiant, calculant sa moyenne et affichant cette moyenne avec la mention 
# ("Très bien" à partir de 16, "Bien" entre 14 et 16, "Assez bien" entre 12 et 14, 
# "Passable" entre 10 et 12, "Insuffisant" en dessous de 10)
# Note entre 0 et 20

N1 = float(input("Entrer la node de premier etudiant : "))
N2 = float(input("Entrer la node de premier etudiant : "))
N3 = float(input("Entrer la node de premier etudiant : "))

S = N1+N2+N3
M = S / 3

if 20 >= M >= 16 :
    print("La moyenne est ",format(M,".2f"),"Très bien!",)
elif 14 <= M < 16 :
    print("La moyenne est ",format(M,".2f"),"Bien!",)
elif 12 <= M < 14 :
    print("La moyenne est ",format(M,".2f"),"Assez bien!",)
elif 10 <= M < 12 :
    print("La moyenne est ",format(M,".2f"),"Passable!",)
elif M < 10 :
    print("La moyenne est ",format(M,".2f"),"Insuffisant",)
else :
    print("ERROR")