import random
def initial ():
    #Proposition au joueur de jouer avec son propre fichier
    proposition = input("Propose un nom de ficher si tu veux utiliser le tiens sinon clique sur 'Entrer' pour utiliser le fichier par defaut :  ")
    if proposition == "":
        fichier = "Motspendu.txt"
    else :
        fichier = proposition
    pendu(fichier)

#création de la fonction
def choisir_mot(fichier):

    with open(fichier, "r") as fichier:  # Ouvre le fichier contenant les mots
        lignes = fichier.readlines()  # Lit toutes les lignes

    mots_sans_accents = []  # Liste pour stocker les mots sans accents

    for mot in lignes:
        mot = mot.strip()  # Supprime les espaces et sauts de ligne
        # Remplace tous les caractères accentués par leur équivalent sans accent
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
        mots_sans_accents.append(mot)  # Ajoute le mot nettoyé à la liste

    return random.choice(mots_sans_accents)  # Retourne un mot aléatoire

# Fonction principale du jeu du pendu
def pendu(fichier):
    print(
        "Bienvenue au jeu du pendu, l'objectif est de trouver le mot caché derrière les '_' vous avez doit à 6 fautes \nA vous de JOUER ! ")

    solution = choisir_mot(fichier)  # Mot à deviner, choisi aléatoirement

    mot_a_trouver = "_" * len(solution)  # Mot affiché avec des "_"
    mot_actualiser = "_" * len(solution)  # Copie pour suivre les changements
    nombre_chance = 6
    joker = 1  # Nombre de jokers disponibles

    print("Trouve le mot du pendu (tu as droit à 6 erreurs)")
    print(mot_a_trouver)  # Affiche le mot sous forme masquée

    while nombre_chance != 0:  # Tant qu’il reste des chances
        lettre = input("Propose une lettre : ")

        # Vérifie chaque lettre du mot solution
        for i, lettres in enumerate(solution):
            if lettre == lettres:
                mot_a_trouver = mot_a_trouver[:i] + lettre + mot_a_trouver[i + 1:] # Remplace les "_" par la lettre si elle est correcte

        if lettre in mot_actualiser: # Si la lettre a déjà été trouvée
            print("La lettre a deja été trouver !")

        elif mot_a_trouver == mot_actualiser:        # Si la lettre ne change rien => mauvaise lettre
            nombre_chance -= 1
            print(f"La lettre {lettre} n'est pas dans le mot... \nIl te reste {nombre_chance} chances")

        elif mot_a_trouver == solution:        # Si toutes les lettres ont été devinées
            print(f"Tu as gagnée le mot était bien : {solution} ")
            break

        else:
            print(f"La lettre {lettre} est bien dans le mot, continue comme ça")            # Si la lettre est correcte mais le mot n'est pas encore complet
            print(mot_a_trouver)

        mot_actualiser = mot_a_trouver  # Met à jour l'état actuel du mot

        if nombre_chance == 1 and joker == 1:        # Utilise le joker si on est à une chance de perdre
            position = mot_actualiser.find("_")  # Trouve une lettre encore inconnue
            print(f"Teste la lettre {solution[position]} pour voir ;)")
            joker -= 1  # Utilisation unique du joker

    # Si le joueur a perdu
    if nombre_chance == 0:
        print(f"Tu as perdu, le mot etait : {solution} ")

    return rejouer(fichier)  # Propose de rejouer après chaque partie

# Fonction qui propose de rejouer
def rejouer(fichier):
    reponse = input("Rejouer ? (yes/no) : ")
    if reponse == "no":
        return print ("Au revoir")
    elif reponse == "yes":
        return pendu(fichier)  # Relance une nouvelle partie
    else:
        print("Vous devez écrire soit yes soit no")        # Si la réponse n'est ni yes ni no
        return rejouer(fichier)  # Redemande une réponse valide

initial()
