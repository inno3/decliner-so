# Décliner la science ouverte

## Modification du 19 et 20/07/2022 par Emilien et Célya

- séparation étape recodage et essai de reproduction pour mettre données brutes diffusables à disposition
- création d'un jupyternotebook `transformation data raw.ipynb` pour obtenir les jeux de données brutes diffusables et non diffusables (non mis sur le gitlab)
- mise à jour du jupyter notebook de reproduction avec information supp, ccl
- mise à jour du gitlab



## Modification du 21/06/2022 par Célya

- passage de Github à Gitlab forge inno3
- travail du ReadMe.md 
- inclusion modification contextualisation

## Modification du 3/06/2022 par EMilien

- transformation arborescence
- amélioration documentation passage FactoMineR

## Modification du 3/06/22 par Célya

- Ajout d'élément de contextualisation au départ
- Changement de nom du fichier de données `21-08_QSO2_pondertion.csv` pour `21-08_QSO2_ponderation.csv`



## Modification du 23/05/22 Réflexion en cours du passage R -> Python par Emilien

Reproduction du jeu de données

- erreur potentielle de recodage : colonne oksoutien, très insatisfait codé en très satisfait
- idem pour limite_temps : ID 1192 codé différemment, d'où vient l'erreur ?
- réduit à 1 de différence pour les disciplines de pondération : d'où vient l'erreur ?
- pas réussi à reproduire fct_autre : comment cette colonne a-t-elle été constituée ?

Par ailleurs

- fonction de R catdes pas encore implémentée avec les pondérations pour Python
- une différence numérique de résultat (+- 0.3 sur le v.test)


