# Exercice 7 : vérifier une adresse courriel

courriel = input("Entrez une adresse courriel : ")

position_arobase = courriel.find("@")

if position_arobase != -1 and "." in courriel[position_arobase + 1:]:
    print("L'adresse courriel semble valide.")
else:
    print("L'adresse courriel n'est pas valide.")
