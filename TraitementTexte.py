from AntiDictionnaire import AntiDictionnaire
from Lemmatisation import Lemmatisation


def traitementTexte(texte, nlp):
    texte = nlp(texte)
    texte = AntiDictionnaire(texte)
    texte = nlp(texte)
    texte = Lemmatisation(texte)
    return texte
