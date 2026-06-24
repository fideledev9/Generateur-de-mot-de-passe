import random
import string
import json

# Etape 1 : générer un mot de passe aléatoire
def generer_mot_de_passe(longueur):
    # Combinaison de tous les types de caractères
    caractere = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    # Sélection aléatoire de 'longueur' caractères
    longueur_lettres = random.choices(caractere, k=longueur)
    # Conversion de la liste en chaîne de caractères
    mot_de_passe = "".join(longueur_lettres)
    return mot_de_passe

# Etape 2 : sauvegarder un mot de passe dans le fichier JSON
def sauvegarder_mot_de_passe(site, mot_de_passe):
    # Lecture des données existantes
    with open("mots_de_passe.json", "r", encoding="utf-8") as f:
        content = f.read()
    # Si le fichier est vide, on part d'un dictionnaire vide
    if content == "":
        donnees = {}
    else:
        donnees = json.loads(content)
    # Ajout du nouveau mot de passe
    donnees[site] = mot_de_passe
    # Sauvegarde dans le fichier
    with open("mots_de_passe.json", "w", encoding="utf-8") as f:
        json.dump(donnees, f)

# Etape 3 : afficher tous les mots de passe sauvegardés
def afficher_mots_de_passe():
    # Lecture du fichier JSON
    with open("mots_de_passe.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)
    # Affichage de chaque site et son mot de passe
    for site, mot_de_passe in donnees.items():
        print(f"{site} : {mot_de_passe}")

# ZONE DE TEST
sauvegarder_mot_de_passe("twitter", generer_mot_de_passe(8))
afficher_mots_de_passe()