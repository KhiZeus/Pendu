"""Le script qui suit permet de réaliser le jeu du pendu ;
    l'utilisateur du jeu joue contre l'ordinateur qui choisit un mot dans un fichier fourni
    Version: 1.1 :  structure simple de devinette d'une lettre dans un mot fixé
    Notes:  Le programme ne s'arrête pas en cas de victoire
    """
import random

"""____________________________________________________

Definitions des fonctions
 ________________________________________________________

"""


def lister_fichier(nom_du_fichier):
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
            mot_incomplet+= caracter
        else:
            mot_incomplet += " _"

    return mot_incomplet


"""____________________________________________________

Main
 ________________________________________________________

"""
liste_mots = []

# choix du fichier avec les mots à deviner
lecture_nom = False
while not lecture_nom:
    decision_ajout_fichier = input("Voulez-vous utilisez votre propre fichier? o = oui   n = non :")
    if decision_ajout_fichier == 'o':
        nom_fichier = input("Entrez le nom de fichier avec son extension : ")
        lecture_nom = True
    elif decision_ajout_fichier == 'n':
        nom_fichier = "mots_pendu.txt"
        lecture_nom = True
    else:
        print("""merci d""'"entrez 'o' pour oui et 'n' pour non""")
# Conversion du fichier lu enliste de mot
liste_mots = lister_fichier(nom_fichier)
# reprise
#definition du mot a deviner
MotObjectif = random.choice(liste_mots)
MotObtenu = ""
for i, car in enumerate(MotObjectif):
    MotObtenu +=" _ "
print(f"voici",MotObtenu)
NombreDeChance = 6
lettre_trouve=[]
lettre_essaies = []
while NombreDeChance > 0 and " _" in MotObtenu:
    print(f"\nLe mot à deviner est : ", MotObtenu, "encore ", NombreDeChance, " chances ;déja essayé",lettre_essaies,"\n ")
    LettrePropose = input("Proposez une lettre: ")
    lettre_essaies.append(LettrePropose)
    if  LettrePropose in MotObjectif:
        lettre_trouve.append(LettrePropose)
        MotObtenu = deviner_mot(lettre_trouve,MotObjectif)
        print("BRAVO !! Vous avez trouver une lettre du mot ")
    else:
        NombreDeChance -= 1
        print(f"OOOPS!! Cette lettre ne se trouve pas dans le mot recherché \n \t \t Essaies restants :",
              NombreDeChance, "\n")

if MotObtenu == MotObjectif:
    print(f" LA PARTIE EST GAGNÉE :) Vous évitez la potence \n Le mot est bien :\t ",MotObtenu)
else:
    print(f"VOUS ETES PENDU !! le mot à trouver étais :\t", MotObjectif)

