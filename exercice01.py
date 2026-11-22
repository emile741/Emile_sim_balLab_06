# Exercice 1 : compter les voyelles d'un mot

mot = input("Entrez un mot : ")

voyelles = "aeiouy"
compteur = 0
for lettre in mot.lower():
    if lettre in voyelles:
        compteur += 1

print(f"Le mot contient {compteur} voyelles.")
