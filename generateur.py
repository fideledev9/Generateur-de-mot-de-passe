import random
import string
import json


def generer_mot_de_passe(longueur):
    caractere = string.ascii_uppercase + string.ascii_lowercase +string.digits + string.punctuation
    longueur_lettres = random.choices(caractere, k = longueur)
    mot_de_passe ="".join(longueur_lettres)
    return mot_de_passe

def sauvegarder_mot_de_passe(site, mot_de_passe):
    with open("mots_de_passe.json", "r" , encoding="utf-8") as f:
        content = f.read()
    if content == "":
        donnees = {}
    else:
        donnees = json.loads(content)
    donnees[site] = mot_de_passe
    with open("mots_de_passe.json", "w" , encoding="utf-8") as f:
        json.dump(donnees, f)

print(sauvegarder_mot_de_passe("facebook", generer_mot_de_passe(8)))