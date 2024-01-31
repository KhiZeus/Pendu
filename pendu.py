import random

"""Le script qui suit permet de réaliser le jeu du pendu ;
    l'utilisateur du jeu joue contre l'ordinateur qui choisit un mot dans un fichier fourni
    Version: 1.1 :  structure simple de devinette d'une lettre dans un mot fixé
    Notes:  Le programme ne s'arrête pas en cas de victoire
    """

"""____________________________________________________

Definitions des fonctions
 ________________________________________________________
"""


def lister_fichier(nom_du_fichier="mots_pendu.txt"):
    """Fonction :Importation de fichier en list
     Argument : nom du fichier"""
    """""""retour   : list des mots"""

    # ouverture de fichier
    with open(nom_du_fichier, "r") as f:
        liste_mot = []
        for line in f:
            # ligne en liste
            ligne = line.split()
            # ajout de la ligne
            liste_mot.extend(ligne)
    # vérification du resultat

    return liste_mot


def deviner_mot(liste_lettre, mot):
    """remplace les lettres du mot manquants dans la liste de lettre par "_"
    Argument:
            Mot 
            liste_llettre"""
    mot_incomplet = ""
    for caracter in mot:
        if caracter in liste_lettre:
            mot_incomplet += caracter
        else:
            mot_incomplet += " _"

    return mot_incomplet

# fonction pour simplifier les text
def simplifier(texte):
    """Remplace les caractère spéciaux dans un texte par des caractères simples:
  enlève les accents, la cédille, ....
  Argument: Texte à simplifier
  return le même text en simple
  """

    correspondance = {
        "àáâãäå": "a",
        "æ": "ae",
        "èéêë": "e",
        "ìíîï": "i",
        "ñ": "n",
        "òóôõöø": "o",
        "œ": "oe",
        "ùúûü": "u",
        "ýÿ": "y",
        "ç": "c"
    }

    texte_simple = ""
    for caracter in texte:
        for complexe_texte, simple in correspondance.items():
            if caracter in complexe_texte:
                texte_simple += simple
                break
        else:
            texte_simple += caracter

    return texte_simple

"""____________________________________________________

Main
 ________________________________________________________
"""

liste_mots = []

# choix du fichier avec les mots à deviner
changement_fichier = "o"
while changement_fichier == "o":

    lecture_nom = False
    essaie_lecture = 0
    while not lecture_nom:
        # l'utilisateur dit s'il veux charger son propre fichier
        decision_ajout_fichier = input("Voulez-vous utilisez votre propre fichier? o = oui   n = non :")
        if decision_ajout_fichier == 'o':
            nom_fichier = input("Entrez le nom de fichier avec son extension : ")
            lecture_nom = True
        elif decision_ajout_fichier == 'n' or essaie_lecture >= 2:
            print("""Utilisons le fichier "mots_pendu.txt""")
            nom_fichier = "mots_pendu.txt"
            lecture_nom = True
        # en cas de frappe differente de o et n l'utilisateur doit reprendre
        else:
            print("""merci d""'"entrez 'o' pour oui et 'n' pour non""")
            essaie_lecture += 1

    # Conversion du fichier lu enliste de mot
    liste_mots = lister_fichier(nom_fichier)

    # POINT de reprise d'une nouvelle séquence de jeu reprise
    reprise = "o"
    while reprise == "o":

        # definition du mot a deviner
        MotObjectif = simplifier(random.choice(liste_mots))

        # Création du mot vide
        MotObtenu = ""
        for i, car in enumerate(MotObjectif):
            MotObtenu += " _ "

        NombreDeChance = 6
        lettre_trouve = []
        lettre_essaies = []

        while NombreDeChance > 0 and "_" in MotObtenu:
            # afficher mot à deviner actualisé
            print(f"\nLe mot à deviner est : ", MotObtenu, "encore ", NombreDeChance, " chances ; déja essayé",
                  lettre_essaies,
                  "\n ")
            LettrePropose = simplifier(input("Proposez une lettre: "))
            if LettrePropose not in lettre_essaies:
                lettre_essaies.append(LettrePropose)
                if LettrePropose in MotObjectif:
                    lettre_trouve.append(LettrePropose)
                    MotObtenu = deviner_mot(lettre_trouve, MotObjectif)
                    print("BRAVO !! Vous avez trouver une lettre du mot ")
                else:
                    NombreDeChance -= 1
                    print(f"OOOPS!! Cette lettre ne se trouve pas dans le mot recherché \n \t \t Essaies restants :",
                          NombreDeChance, "")
            else:
                print("la lettre a déjà été proposée")

        if MotObtenu == MotObjectif:
            print(f" LA PARTIE EST GAGNÉE :) Vous évitez la potence \n Le mot est bien :\t ", MotObtenu)
        else:
            print(f"VOUS ETES PENDU !! le mot à trouver étais :\t", MotObjectif)

        reprise = input("Voulez vous rejouer ? o = oui   n = non :")
        if reprise == "o":
            changement_fichier = input("Voulez vous changer de fichier ? o = oui   n = non :")
        else:
            changement_fichier = ("n")
