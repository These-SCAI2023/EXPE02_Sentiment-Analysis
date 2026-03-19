from generictools import *

def traiter_dossier(base_path):
    """
    Traite tous les sous-dossiers contenant des fichiers *.txt dans base_path
    """

    start = time.perf_counter()
    for folder in glob.glob(base_path):
        print("Base path:", folder)#Affiche le chemin vers le dossier d'entrée

        SA_repo_creat(folder)#Créer le dossier SA dans le dossier d'entrée
        for txt_file in glob.glob(folder + "/*.txt"):#Lit tous les fichiers *.txt présents
            outputname = filename_output(txt_file) #Définit le nom du fichier de sortie
            sa_path = f"{folder}/SA/{outputname}" #Définit le chemin pour le fichier de sortie
            # Vérifie si le fichier SA existe déjà
            if os.path.exists(sa_path):
                print(f"SA déjà calculé pour {txt_file}, passage au suivant.")
                continue  # passe au fichier suivant
            #Lire le texte dans le fichier
            texte = lire_fichier(txt_file)

            #Segmente le texte
            segments_txt = segmentation(texte)

            segments = {}  #initialise le dictionnaire dans lequel stocker les dictionnaires comportant les phrases et les analyses
            for idx, seg in enumerate(segments_txt):
                print("Segment analyser : ",seg)
                print("analyse : ",  analise_sent(seg))
                segments[f"segment {idx}"] = {
                    "texte": seg,
                    "analyse": analise_sent(seg)
                }

            #Stocker les résultats
            stocker(f"{folder}/SA/{outputname}", segments)
            end = time.perf_counter()
            #Afficher le temps du calcul
            print(f"Temps écoulé : {end - start:.3f} secondes")
            d = {"Temps écoulé": f"{end - start:.3f}"}
            stocker(f"{folder}/SA/{outputname}_time.json",d)

 #Chemin relatif vers les documents
corpus = "../small-ELTeC-fra-2021-2024_ENSAAMA2026/*/"

# Traitement des dossiers REF
traiter_dossier(corpus + "*REF")

# Traitement des dossiers OCR
traiter_dossier(corpus + "/*OCR/*")






