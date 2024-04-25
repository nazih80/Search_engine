from Recherche import Recherche
import spacy
from flask import Flask, render_template, request
app = Flask(__name__)
nlp = spacy.load("fr_core_news_sm")


@app.route("/", methods=["GET"])
def home():
    requête = request.args.get("requête")
    if requête:
        résultat = Recherche(requête, nlp)
        if len(résultat) == 0:
            return render_template("index.html", introuvable = True)
        else:
            return render_template("index.html", résultat = résultat, requête = requête)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
