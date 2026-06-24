from generateur import *

menu = ["1. Générer et sauvegarder un mot de passe",
        "2. Afficher tous les mots de passe",
        "3. Rechercher un mot de passe",
        "4. Supprimer un mot de passe",
        "5. Quitter"]
while True:
    print("Choisissez parmi les options suivantes")
    for option in menu:
        print(option)
    choix = input()
    while choix not in ["1", "2", "3", "4", "5"]:
        print("Choisissez parmi les options suivantes")
        for option in menu:
            print(option)
        choix = input()
    if choix == "1":
        site = input("Nom du site : ")
        longueur = int(input("Longueur du mot de passe : "))
        mot_de_passe = generer_mot_de_passe(longueur)
        sauvegarder_mot_de_passe(site, mot_de_passe)
        print(f"Mot de passe généré et sauvegardé : {mot_de_passe}")
    elif choix == "2":
        afficher_mots_de_passe()
    elif choix == "3":
        site = input("Nom du site : ")
        rechercher_mot_de_passe(site)
    elif choix == "4":
        site = input("Nom du site : ")
        supprimer_mot_de_passe(site)
    elif choix == "5":
        break

