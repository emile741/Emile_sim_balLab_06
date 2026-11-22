# Exercice 9 : afficher le mot le plus long d'une phrase

phrase = input("Entrez une phrase : ")

mots = phrase.split()
mot_le_plus_long = ""
for mot in mots:
    if len(mot) > len(mot_le_plus_long):
        mot_le_plus_long = mot

print(f"Mot le plus long : {mot_le_plus_long}")
