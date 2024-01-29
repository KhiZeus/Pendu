"""Le script qui suit permet de réaliser le jeu du pendu ;
    l'utilisateur du jeu joue contre l'ordinateur qui choisit un mot dans un fichier fourni
    Version: 1.1 :  structure simple de devinette d'une lettre dans un mot fixé
    """
MotObjectif = "bonjour"
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
