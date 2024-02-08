# Écrivez un programme Python, entrez deux nombres de l'utilisateur et 
# trouvez le plus grand diviseur commun en utilisant la boucle for.

A = int(input("Entrer le nombre de A : "))
B = int(input("Entrer le nombre de B : "))
min = A if (A < B) else B

for i in range(1, min+1):
    if (A % i == 0 and B % i == 0):
        pgcd = i
print("PGCD de {0} et {1} = {2}".format(A, B, pgcd))


