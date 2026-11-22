# Exercice 10 : masquer un numéro de carte de crédit

numero = input("Entrez votre numéro de carte de crédit : ")

numero_masque = "*" * (len(numero) - 4) + numero[-4:]

print(f"Numéro masqué : {numero_masque}")
