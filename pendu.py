"""Le script qui suit permet de réaliser le jeu du pendu ;
    l'utilisateur du jeu joue contre l'ordinateur qui choisit un mot dans un fichier fourni
    Version: 1.1 :  structure simple de devinette d'une lettre dans un mot fixé
    Notes:  Le programme ne s'arrête pas en cas de victoire
    """
"""____________________________________________________

Definitions des fonctions
 ________________________________________________________

""""Fonction :Importation de fichier en list"""
""" Argument : nom du fichier"""
"""""""retour   : list des mots"""
def lister_fichier(nom_du_fichier):
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


"""____________________________________________________

Main
 ________________________________________________________

"""
liste_mots = []
MotObjectif = "bonjour"

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

liste_mots = lister_fichier(nom_fichier)
NombreDeChance = 6
MotObtenu = "_ _ _ _ _ _ _ "
while NombreDeChance > 0:  # "_" in MotObtenu and
    LettrePropose = input("Proposez une lettre: ")
    if LettrePropose in MotObjectif:
        print("BRAVO !! Vous avez trouver une lettre du mot ")
    else:
        NombreDeChance -= 1
        print(f"OOOPS!! Cette lettre ne se trouve pas dans le mot recherché \n \t \t Essaies restants :",
              NombreDeChance, "\n")
