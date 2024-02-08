# Une boutique propose à ces clients, une réduction de 15% pour 
# les montants d’achat supérieurs à 200 dh. Écrire un programme Python 
# permettant de saisir le prix total HT et de calculer le  montant TTC 
# en prenant en compte la réduction et la TVA=20%.  


def Discount () :
    if A >= 200 :
        B = (A - (A * 0.15)) + A *0.2
        print(" - Le prix total est : ",B," DH")
    else :
        C = A + A *0.2
        print(" - Le prix total est : ",C," DH")

def TVA () :
    TVA = A * 0.2
    print(" - TVA : ",TVA," DH")

def D_Amount () :
    if A >= 200 :
        D = A * 0.15
        print(" - Discount :",D," DH")
    else :
        print(" - Discount : - ")

A = int (input("Veuillez entrer la somme total : "))

print("------------")
print("                  ")
print("  WELCOME  ")
print(" *********  ")
Discount()
TVA ()
D_Amount ()
print("                  ")
print("                  ")
