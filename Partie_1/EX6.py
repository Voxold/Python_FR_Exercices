
# Nous allons écrire un programme qui demande à l'utilisateur
#  de taper 5 notes et qui affiche leur somme et leur moyenne.

N1 = float(input("Entrer la note 1 :"))
N2 = float(input("Entrer la note 2 :"))
N3 = float(input("Entrer la note 3 :"))
N4 = float(input("Entrer la note 4 :"))
N5 = float(input("Entrer la note 5 :"))

Somme = N1+N2+N3+N4+N5
Moyenne = Somme / 5

print("La somme est : ",format(Somme,".2f"))
print("La moyenne est : ",format(Moyenne,".2f"))

