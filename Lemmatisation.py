def Lemmatisation(texte):
    texte = [mot.lemma_ for mot in texte]
    return " ".join(texte)
