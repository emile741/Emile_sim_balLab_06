# Exercice 6 : valider un nom d'utilisateur

nom = input("Entrez un nom d'utilisateur : ")

if nom.isalnum() and len(nom) >= 5:
    print("Le nom d'utilisateur est valide.")
else:
    print("Le nom d'utilisateur n'est pas valide.")
    if not nom.isalnum():
        print("- Il doit contenir uniquement des lettres et des chiffres.")
    if len(nom) < 5:
        print("- Il doit posséder au moins 5 caractères.")
