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


def pendu():
    print(
        "Bienvenue au jeu du pendu, l'objectif est de trouver le mot caché derrière les '_' vous avez doit à 6 fautes /n à vous de JOUER ! ")

    solution = choisirmot()

    mot_a_trouver = "_" * len(solution)
    mot_actualiser = "_" * len(solution)
    nombre_chance = 6
    joker = 1

    print("Trouve le mot du pendu (tu as droit à 6 erreurs)")
    print(mot_a_trouver)

    while nombre_chance != 0:
        lettre = input("Propose une lettre : ")
        for i, lettres in enumerate(solution):
            if lettre == lettres:
                mot_a_trouver = mot_a_trouver[:i] + lettre + mot_a_trouver[i + 1:]

        if lettre in mot_actualiser:
            print("La lettre a deja été trouver !")
        elif mot_a_trouver == mot_actualiser:
            nombre_chance -= 1
            print(f"il vous reste {nombre_chance} chances")
        elif mot_a_trouver == solution:
            print(f"Tu as gagnée le mot était bien : {solution} ")
            break
        else:
            print("Continue comme ça")
            print(mot_a_trouver)
        mot_actualiser = mot_a_trouver

        if nombre_chance == 1 and joker == 1:
            position = mot_actualiser.find("_")
            print(f"Teste la lettre {solution[position]} pour voir ;)")
            joker -= 1

    if nombre_chance == 0:
        print(f"Tu as perdu, le mot etait : {solution} ")
    return rejouer()

def rejouer():
    reponse = input("Rejouer ? (yes/no) : ")
    if reponse == "no":
        print ("Au revoir")
    elif reponse == "yes":
        return pendu()
    else:
        print("Vous devez écrire soit yes soit no")
        return rejouer()

pendu()
