"""Le script qui suit permet de réaliser le jeu du pendu ;
    l'utilisateur du jeu joue contre l'ordinateur qui choisit un mot dans un fichier fourni
    Version: 1.1 :  structure simple de devinette d'une lettre dans un mot fixé
    Notes:  Le programme ne s'arrête pas en cas de victoire
    """
"""____________________________________________________

Definitions des fonctions
 ________________________________________________________
"""


def lister_fichier(nom_du_fichier):
    """"Fonction :Importation de fichier en list"""
    """ Argument : nom du fichier"""
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
    # print(liste_mot)
    return liste_mot


"""def choisir_mot(liste_mot):
    """"Fonction qui choisis de manière random uneleme"""
""" Argument : nom du fichier"""
"""""""retour   : list des mots"""
"""____________________________________________________

Main
 ________________________________________________________

"""
import random
# Declaration des constantes
liste_mots = []

NombreDeChance = 6

# choix du fichier avec les mots à deviner

lecture_nom = False
while not lecture_nom:
    # l'utilisateur dit s'il veux charger son propre fichier
    decision_ajout_fichier = input("Voulez-vous utilisez votre propre fichier? o = oui   n = non :")
    if decision_ajout_fichier == 'o':
        nom_fichier = input("Entrez le nom de fichier avec son extension : ")
        lecture_nom = True
    elif decision_ajout_fichier == 'n':
        nom_fichier = "mots_pendu.txt"
        lecture_nom = True
    # en cas de frappe differente de o et n l'utilisateur doit reprendre
    else:
        print("""merci d""'"entrez 'o' pour oui et 'n' pour non""")

# ouverture du fichier et stockage dans une liste
list_fichier = lister_fichier(nom_fichier)

# choix du mot
MotObjectif = random.choice(list_fichier)
print(MotObjectif)

while NombreDeChance > 0:  # "_" in MotObtenu and
    #afficher mot à deviner actualisé
    LettrePropose = input("Proposez une lettre: ")
    if LettrePropose in MotObjectif:
        print("BRAVO !! Vous avez trouver une lettre du mot ")
    else:
        NombreDeChance -= 1
        print(f"OOOPS!! Cette lettre ne se trouve pas dans le mot recherché \n \t \t Essaies restants :",
              NombreDeChance, " \n")
