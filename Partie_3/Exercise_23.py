#  Écrivez un programme Python pour entrer un nombre et vérifiez si 
#le nombre est parfait ou non.
#Un nombre parfait est un entier positif qui est égal à la somme de ses
#diviseurs positifs appropriés.
#Par exemple: 6 est le premier nombre parfait
#Les diviseurs appropriés de 6 sont 1, 2, 3.
#Somme de ses diviseurs stricts = 1 + 2 + 3 = 6.
#Par conséquent, 6 est un nombre parfait.   

N = int(input("Saisir un nombre : "))

S = 0
for i in range(1, N):
    
    if (N % i == 0):
        S += i

if (S == N):
    print(N, "est un nombre parfait")
else:
    print(N, "n'est pas un nombre parfait")