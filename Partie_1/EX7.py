
# Nous allons écrire un programme qui demande à l'utilisateur 
#de taper le rayon d’une sphère, puis calcule et affiche son volume.

R = int(input("Entrer le Rayon :"))

R2 = R ** 3
Volume = ((4*3.14*R2) / 3)

print("Le volume est : ",format(Volume,".2f"))

