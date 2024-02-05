
# Nous allons écrire un programme opérations qui calcule 
# la somme, le produit, la différence et la division de deux nombre réels.

A = int(input("Entre premiere numero :"))
B = int(input("Entre deuxieme numero :"))

S = A + B
P = A * B
D = A - B 
Div = A / B

print("A + B = ",S)
print("A * B = ",P)
print("A - B = ",format(D,".2f"))
print("A / B = ",format(Div,".2f"))

# format(Div,".2f") ==> pour vergul