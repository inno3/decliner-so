# [Decliner-SO] Décliner la science ouverte : 

## Description 

Ensemble des resources ayant servi à l'analyse du questionnaire "données et science ouverte" de l'étude Décliner la science ouverte (Decliner-SO) dans une démarche de reproductibilité. 
Pour en savoir plus sur l'étude et ses résultats : https://declinerso.pubpub.org/ + résumé de l'étude sur [HAL](https://hal-lara.archives-ouvertes.fr/hal-03798504v1).

## Navigation 

Vous trouverez dans ce projet : 
- `Data` avec le jeu de données brutes (après anonymisation) disponible également sur [recherche.data.gouv](https://entrepot.recherche.data.gouv.fr/dataset.xhtml?persistentId=doi:10.57745/V64RYT).
- `Scripts`
    - le jupyter notebook d'Emilien Schultz explicitant la démarche de reproductibilité de l'analyse initiale (passage de R à Python) ;
    - les fonctions pyr.py supplémentaires (nouvelles fonctions pour s'adapter aux bibliothèques R) ;
    - un fichier log.md de suivi de modification (ce projet a fait l'objet de différentes itérations entre l'équipe projet et Emilien).
- `Méthodo` 
    - une note méthodologique pour documenter l'analyse initiale et qui a servi de base au travail de reproductibilité.


## Contribution

L’étude Décliner la science ouverte (Decliner-SO) a été réalisée dans le cadre de la mission « Réussir l’appropriation de la science ouverte » pour le Comité pour la science ouverte (CoSO). Elle a été portée par un groupe de travail multi-disciplinaire et professionnel du collège « données de la recherche ». Pour la liste de l'ensemble des membres du groupe de travail, consultez la page du projet sur [ouvrirlascience.fr](https://www.ouvrirlascience.fr/reussir-lappropriation-de-la-science-ouverte/?menu=4). 

L'analyse du questionnaire "données et science ouverte" a été réalisée collectivement par 
- Claire Lemercier (CNRS - CSO/SciencePo) pour l'analyse statistique sur R ;
- Célya Gruson-Daniel (INNO3 - COSTECH/UTC) pour l'articulation avec l'analyse qualitative.

La démarche de reproductibilité avec la réalisation du _notebook_ python et des fonctions supplémentaires a été réalisée par Emilien Schultz (Medialab/SciencePo) avec un travail d'itération avec Célya Gruson-Daniel et Claire Lemercier.

## License

Le contenu texte est publié en licence CC-BY 4.O. Les scripts et les données sont publiés en licence Ouverte 2.0.
