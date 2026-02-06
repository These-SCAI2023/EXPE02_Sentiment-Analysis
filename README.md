# Evaluation de modèle d'analyse de sentiments sur données bruitées

Analyse de sentiments sur le corpus [small_ELTeC-fra](https://github.com/These-SCAI2023/EXPE44_CORPUS_EVAL/tree/main) avec [Distilcamembert Base Sentiment](https://model.aibase.com/models/details/1915694195572105217?utm_source=chatgpt.com) et [french-sentiment-analysis-with-bert](https://github.com/TheophileBlard/french-sentiment-analysis-with-bert?tab=readme-ov-file).

Avec **Distilcamembert Base Sentiment** Le 6 février 2026 : 

| Book (Author) | # Tokens | REF | Kraken| Kraken4.3.13 |LectaurepKraken4.3.13 |Tesseract|Tesseract3.10|
|--------------|---------:|-----:|------:|-------------:|---------------------:|--------:|------------:|
| *Mon village* (J. Adam) | 20 938  | 🗸||🗸 |🗸|||
| *Marie-Claire* (M. Audoux) | 35 780  | || ||||
| *Le château de Pinon, vol. I* (G. A. Dash) | 44 246  | || ||||
| *La petite Jeanne* (Z. Carraud) | 53 212  | || ||||
| *La nouvelle espérance* (A. de Noailles) | 54 272  | || ||||
| *Une vie* (G. de Maupassant) | 75 745  | || ||||
| *Albert Savarus. Une fille d’Ève* (H. de Balzac) | 79 924  | || ||||
| *Le petit chose* (A. Daudet) | 86 482  | || ||||
| *Les trappeurs de l’Arkansas* (G. Aimard) | 91 119  | || ||||
| *La Belle rivière* (G. Aimard) | 137 392  | || ||||
| *L’Éducation sentimentale* (G. Flaubert) | 150 494  | || ||||

# Description Expe

## Installation : environnement python 3.9

J'ai travaillé dans un environnement python 3.9 car version de Tensorflow plus supporté/maintenu par Hugginface après python 3.9

## Segmentation avec spaCy 3.7

J'ai fais une segmentation par phrase, car les exemple montre des phrases. Segmentation avec le modèle "fr_core_news_lg". On pourrait faire un autre type de découpe.




