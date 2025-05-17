import random
def choisirmot():
    with open("Motspendu.txt", "r") as fichier:
        lignes = fichier.readlines()
    mots_sans_accents = []
    for mot in lignes:
        mot = mot.strip()
        mot = mot.replace('à', 'a')
        mot = mot.replace('â', 'a')
        mot = mot.replace('ä', 'a')
        mot = mot.replace('é', 'e')
        mot = mot.replace('è', 'e')
        mot = mot.replace('ê', 'e')
        mot = mot.replace('ë', 'e')
        mot = mot.replace('î', 'i')
        mot = mot.replace('ï', 'i')
        mot = mot.replace('ô', 'o')
        mot = mot.replace('ö', 'o')
        mot = mot.replace('ù', 'u')
        mot = mot.replace('û', 'u')
        mot = mot.replace('ü', 'u')
        mot = mot.replace('ç', 'c')
        mots_sans_accents.append(mot)
    return random.choice(mots_sans_accents)