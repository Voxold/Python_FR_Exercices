
# 1 + 2 + 3 + 4 + 5 ... = Somme

A = int ( input ("Entrer le nombre strictement  superieur a 1 :"))

while A <= 1 :
    A = int ( input ("Entrer le nombre strictement  superieur a 1 :")) 

S = 0
i = 1  

while i <= A :
    S = S +i
    i = i + 1

print("La result de la somme est : ",S)
 