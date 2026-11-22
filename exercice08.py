# Exercice 8 : compter les lettres, les chiffres et les espaces

chaine = input("Entrez une chaîne de caractères : ")

lettres = 0
chiffres = 0
espaces = 0
for caractere in chaine:
    if caractere.isalpha():
        lettres += 1
    elif caractere.isdigit():
        chiffres += 1
    elif caractere == " ":
        espaces += 1

print(f"Nombre de lettres : {lettres}")
print(f"Nombre de chiffres : {chiffres}")
print(f"Nombre d'espaces : {espaces}")
