import glob
from generictools import *

i = 0
dic_seg = {}
corpus = "../small-ELTeC-fra-2021-2024_REN/ADAM"

for path in glob.glob(corpus + "/*REF/*court.txt"):
    # print(path)
    texte = lire_fichier(path)

txt_seg = segmentation(texte)
# print(txt_seg)

for seg in txt_seg:
    # print(seg)
    dic_seg[f"segment {i}"] = {}
    dic_seg[f"segment {i}"]["texte"] = seg
    # print(f"segment {i}",seg)
    resultat = analise_sent(seg)
    dic_seg[f"segment {i}"]["analyse"] = resultat
    # print(resultat)
    i += 1
print(dic_seg)
stocker(f"{path}_sa.json",dic_seg)

