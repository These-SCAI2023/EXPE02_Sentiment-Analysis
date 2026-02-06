from generictools import *

corpus = "../small-ELTeC-fra-2021-2024_REN/ADAM/"

# Traitement des dossiers REF
traiter_dossier(corpus + "*REF")

# Traitement des dossiers OCR
traiter_dossier(corpus + "/*OCR/*")

## A optimiser
# for refpath in glob.glob(corpus + "/*REF"):
#     SA_repo_creat(refpath)
#     i = 0
#     dic_seg_ref = {}
#     for subpath in glob.glob(refpath + "/*court.txt"):
#         outputname = filename_output(subpath)
#         texte = lire_fichier(subpath)
#     txt_seg = segmentation(texte)
#     # print(txt_seg)
#
#     for seg in txt_seg:
#         # print(seg)
#         dic_seg_ref[f"segment {i}"] = {}
#         dic_seg_ref[f"segment {i}"]["texte"] = seg
#         # print(f"segment {i}",seg)
#         resultat = analise_sent(seg)
#         dic_seg_ref[f"segment {i}"]["analyse"] = resultat
#         # print(resultat)
#         i += 1
#     print(dic_seg_ref)
#     stocker(f"{refpath}/SA/{outputname}", dic_seg_ref)
#
# for ocrpath in glob.glob(corpus + "/*OCR/*"):
#     SA_repo_creat(ocrpath)
#     dic_seg_ocr = {}
#     ii = 0
#     for subpath in glob.glob(ocrpath + "/*court.txt"):
#         outputname = filename_output(subpath)
#         texte = lire_fichier(subpath)
#     txt_seg = segmentation(texte)
#     # print(txt_seg)
#
#     for seg in txt_seg:
#         # print(seg)
#         dic_seg_ocr[f"segment {ii}"] = {}
#         dic_seg_ocr[f"segment {ii}"]["texte"] = seg
#         resultat = analise_sent(seg)
#         dic_seg_ocr[f"segment {ii}"]["analyse"] = resultat
#         # print(resultat)
#         ii += 1
#     print(dic_seg_ocr)
#     stocker(f"{ocrpath}/SA/{outputname}", dic_seg_ocr)




