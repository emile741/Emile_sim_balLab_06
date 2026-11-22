# Exercice 4 : vérifier si un mot est un palindrome

mot = input("Entrez un mot : ")

mot_normalise = mot.lower()
if mot_normalise == mot_normalise[::-1]:
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")
