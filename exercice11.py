# Exercice 11 : masquer un numéro de carte de crédit avec validations

numero = input("Entrez votre numéro de carte de crédit : ")

# Supprimer les espaces et les tirets
numero = numero.replace(" ", "").replace("-", "")

if not numero.isdigit():
    print("Erreur : le numéro de carte doit contenir uniquement des chiffres.")
elif len(numero) < 16:
    print(f"Erreur : le numéro contient {len(numero)} chiffres, il en manque {16 - len(numero)} (16 requis).")
elif len(numero) > 16:
    print(f"Erreur : le numéro contient {len(numero)} chiffres, soit {len(numero) - 16} de trop (16 requis).")
else:
    numero_masque = "*" * 12 + numero[-4:]
    print(f"Numéro masqué : {numero_masque}")
