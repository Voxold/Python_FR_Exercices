# Fonctions de signes : avec arguments | sans return
# Fonctions de Minimal : avec arguments | avec return
# Fonctions de Maximal : avec arguments | avec return

# Fonctions de signes :
def Signe (A,B) :
    if A * B < 0 :
        print("==> Les deux nombres ont la deffirents signes")
    else :
        print("==> Les deux nombres ont la meme signes")

# Fonctions de Min :
def Min(A,B) :
    if A > B :
        print("==> Le Min des nombres est B")
    elif B > A :
        print("==> Le Min des nombres est A")
    else :
        print("==> Les nombres sont egalement!")
    return(A,B)

# Fonctions de Max :
def Max(A,B) :
    if A > B :
        print("==> Le Max des nombres est A")
    elif B > A :
        print("==> Le Max des nombres est B")
    else :
        print("==> Les nombres sont egalement!")
    return(A,B)

# Appele les fonctions :
A = int(input("Entrer la valeur de A :"))
B = int(input("Entrer la valeur de B :"))
Signe(A,B)
Min(A,B)
Max(A,B)
print("Merci pour votre d'utilisation du programme!")

