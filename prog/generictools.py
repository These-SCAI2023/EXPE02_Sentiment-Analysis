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
    return chaine

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

def traiter_dossier(base_path):
    """
    Traite tous les sous-dossiers contenant des fichiers *court.txt* dans base_path
    """
    print("Base path:", base_path)
    start = time.perf_counter()
    for folder in glob.glob(base_path):
        print(folder)

        SA_repo_creat(folder)
        for txt_file in glob.glob(folder + "/*.txt"):
            outputname = filename_output(txt_file)
            sa_path = f"{folder}/SA/{outputname}"
            # Vérifie si le fichier SA existe déjà
            if os.path.exists(sa_path):
                print(f"SA déjà calculé pour {txt_file}, passage au suivant.")
                continue  # passe au fichier suivant

            texte = lire_fichier(txt_file)
            segments_txt = segmentation(texte)

            segments = {}
            for idx, seg in enumerate(segments_txt):
                segments[f"segment {idx}"] = {
                    "texte": seg,
                    "analyse": analise_sent(seg)
                }

            print(segments)
            stocker(f"{folder}/SA/{outputname}", segments)
            end = time.perf_counter()
            print(f"Temps écoulé : {end - start:.3f} secondes")
            d = {"Temps écoulé": f"{end - start:.3f}"}
            stocker(f"{folder}/SA/{outputname}_time.json",d)




## Tests pour la segmentation avec spaCy
# i = 0
# ii = 0
# nlp = spacy.load("fr_core_news_lg")
# doc1 = nlp("UNE VEILLÉE. Depuis un nombre innombrable d'hivers, c'est dans la maison de Norine Duclos qu'ont lieu les plus égayantes veillées de notre village. Adonc, certain soir, comme j'entrais chez Norine, je la trouvai en train de prêcher ses trois petiotes. — Hé ! Mandine, criait-elle, dépêche-toi de balayer la maison ; plus vite que ça ! Surtout n'oublie pas le coin où la femme de Jean-Claude a épluché une pomme ce matin.")
# doc2 = nlp("UNE YEILLEE. Depuis un nombre innombrable d'hivers, c'est dans la maison de Norine Duclos qu'ont lieu les plus egayantes veilles de notre vil-lage. Adonc, certain soir, comme j'entrais chez Norine, je la trouvai en train de precher ses trois petiotes.- He MIandine, criait-elle, dpeche-toi de balayer la maison ; plus vite que cal Sur-tout n'oublie pas le coin oi la femme de Jean-Claude a epluchc une pomme ce matin.")
# assert doc1.has_annotation("SENT_START")
# print("____________________")
# print("DOC 1 : ")
# print("____________________")
# for sent in doc1.sents:
#
#     print(f"phrase {i} : ",sent.text)
#     i=i+1
#
# assert doc2.has_annotation("SENT_START")
# print("____________________")
# print("DOC 2 : ")
# print("____________________")
# for sent in doc2.sents:
#     print(f"phrase {ii} : ",sent.text)
#     ii=ii+1