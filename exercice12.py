# Exercice 12 : vérifier la robustesse d'un mot de passe

mot_de_passe = input("Entrez un mot de passe : ")

a_majuscule = False
a_minuscule = False
a_chiffre = False
a_special = False

for caractere in mot_de_passe:
    if caractere.isupper():
        a_majuscule = True
    elif caractere.islower():
        a_minuscule = True
    elif caractere.isdigit():
        a_chiffre = True
    elif not caractere.isspace():
        a_special = True

criteres = [
    ("Au moins 8 caractères", len(mot_de_passe) >= 8),
    ("Une lettre majuscule", a_majuscule),
    ("Une lettre minuscule", a_minuscule),
    ("Un chiffre", a_chiffre),
    ("Un caractère spécial (!, @, #, $, %, etc.)", a_special),
]

print("\nCritères respectés :")
for nom, respecte in criteres:
    if respecte:
        print(f"  {nom}")

print("\nCritères non respectés :")
for nom, respecte in criteres:
    if not respecte:
        print(f"  {nom}")

if all(respecte for _, respecte in criteres):
    print("\nLe mot de passe est valide.")
else:
    print("\nLe mot de passe n'est pas valide.")
