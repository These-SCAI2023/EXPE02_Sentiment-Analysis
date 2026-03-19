import glob
import spacy
import json
from transformers import pipeline
from pathlib import Path
import os
import time

def lire_fichier (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    return chaine[:1000]

def filename_output(path):
    filename = path.split('/')[-1] + "_sa.json"
    return filename

def SA_repo_creat(chemin):
    # Crée un objet Path pour le nouveau dossier
    dossier = Path(f"{chemin}/SA")
    # Crée le dossier
    dossier.mkdir(exist_ok=True)  # exist_ok=True évite l'erreur si le dossier existe

def stocker(chemin, contenu):
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()
    return chemin

def segmentation(text):
    nlp = spacy.load("fr_core_news_lg")
    liste_seg = []
    doc = nlp(text)
    assert doc.has_annotation("SENT_START")
    for sent in doc.sents:
        nseg_txt = sent.text
        liste_seg.append(nseg_txt)
    return liste_seg

def analise_sent(phrase):
    analyzer = pipeline(
        task='text-classification',
        model="cmarkea/distilcamembert-base-sentiment",
        tokenizer="cmarkea/distilcamembert-base-sentiment"
    )
    result = analyzer(
        phrase,
        # return_all_scores=True
        top_k=None
    )

    # print(result)
    return result


