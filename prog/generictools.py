import spacy
import json
from transformers import pipeline

def lire_fichier (chemin):
    f = open(chemin , encoding = 'utf−8')
    chaine = f.read ()
    f.close ()
    return chaine

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