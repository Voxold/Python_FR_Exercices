
S = 0 
for i in range(1,9) :
    print("Entrer nombre ",i," : ",end="")
    A = int(input())
    if A < 0 :
        break
    S = S + A
print("La somme des nombres positives est : ",S)

