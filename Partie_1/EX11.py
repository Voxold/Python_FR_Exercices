
#Dans cette vidéo, nous allons écrire un programme qui affiche la résistance 
# équivalente à trois résistances R1, R2, R3 :
# - si les résistances sont branchées en série.
# - si les résistances sont branchées en parallèle.

R1 = int(input("Entrer la valeur de premiere resistance : "))
R2 = int(input("Entrer la valeur de deuxieme resistance : "))
R3 = int(input("Entrer la valeur de troisieme resistance : "))

RS = R1 + R2 + R3
RP = (R1*R2*R3) / ((R1*R2)+(R1*R3)+(R2*R3))

print("Valeur de resistance total en serie : R.Serie = ",format(RS,".2f"))
print("Valeur de resistance total en serie : R.Par = ",format(RP,".2f"))