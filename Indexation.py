from TraitementTexte import traitementTexte
import os
import pymysql
from PyPDF2 import PdfReader
import spacy


def Indexation():
    connection = pymysql.connect(
        host="localhost", user="root", password="admin", database="moteur_recherche")
    cursor = connection.cursor()

    répertoire = "static/"
    for nomFichier in os.listdir(répertoire):
        if nomFichier.endswith(".pdf"):
            emplacementFichier = os.path.join(répertoire, nomFichier)
            with open(emplacementFichier, "rb") as f:
                fichierPDF = PdfReader(f)
                texte = ""
                for numéroPage in range(len(fichierPDF.pages)):
                    texte += fichierPDF.pages[numéroPage].extract_text().lower()
                texte = traitementTexte(texte, spacy.load("fr_core_news_sm"))
            titre = nomFichier.split('.')[0]

            cursor.execute("INSERT INTO documents (titre, contenu) VALUES (%s, %s)",
                           (titre, texte))
    connection.commit()
    connection.close()


Indexation()
