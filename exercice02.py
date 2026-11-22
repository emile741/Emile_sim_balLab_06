# Exercice 2 : compter les majuscules et les minuscules d'une phrase

phrase = input("Entrez une phrase : ")

majuscules = 0
minuscules = 0
for caractere in phrase:
    if caractere.isupper():
        majuscules += 1
    elif caractere.islower():
        minuscules += 1

print(f"Majuscules : {majuscules}")
print(f"Minuscules : {minuscules}")
