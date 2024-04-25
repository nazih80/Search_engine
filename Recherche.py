from TraitementTexte import traitementTexte
import pymysql


def Recherche(requête, nlp):
    connection = pymysql.connect(
        host="localhost", user="root", password="admin", database="moteur_recherche")
    curseur = connection.cursor()
    requête = traitementTexte(requête, nlp)
    curseur.execute(
        "SELECT titre FROM documents WHERE MATCH(contenu) AGAINST ((%s) IN NATURAL LANGUAGE MODE)", (requête,))
    résultat = curseur.fetchall()
    connection.close()
    return [résultat[i][0] for i in range(len(résultat))]
