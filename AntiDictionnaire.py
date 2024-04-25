import json


def AntiDictionnaire(texte):
    with open("AntiDictionnaire.json") as f:
        anti_dictionnaire = json.load(f)
    texte = [mot.text for mot in texte if mot.text not in anti_dictionnaire]
    return ' '.join(texte)
