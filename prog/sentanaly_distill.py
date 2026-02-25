from generictools import *

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


corpus = "../small-ELTeC-fra-2021-2024_REN/*/"

# Traitement des dossiers REF
traiter_dossier(corpus + "*REF")

# Traitement des dossiers OCR
traiter_dossier(corpus + "/*OCR/*")

# for path in glob.glob(corpus + "/*/*"):
#     print(path)





