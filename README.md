# AstroImagePy

## Prérequis
- Installer [Anaconda](https://www.anaconda.com/download/) (v5.3+) ou [Miniconda](https://conda.io/miniconda.html) (v4.5+)

## Installation de l'environnement
Dans une fenêtre de commande "conda prompt" :
- Se placer dans le répertoire d'AstroImagePy : `cd "/path/to/astro-image-py"`
- Créer l'environnement : `conda env create -f environment.yml`

## Lancement de l'outil
Dans une fenêtre de commande "conda prompt" :
- Se placer dans le répertoire d'AstroImagePy : `cd "/path/to/astro-image-py"`
- Activer l'environnement: `conda activate astro-image-py` 
- Lancer l'outil: `python src/main.py ./images`

## Images à prendre
(En prendre un dizaine pour chaque catégorie)
- **Flats** : images d'une lumière diffuse (la plus uniforme possible) avec une exposition à 2/3 de l'histogramme.<br>
Les **Flats** permettent de corriger les défauts d'uniformité du capteur.
- **Offsets** : images prises sans objectif, avec le capuchon de l'appareil, avec le temps d'exposition le plus court possible.<br>
Les **Offsets** permettent de corriger le bruit électronique du capteur.
- **Images** : les images du ciel, prises avec les mêmes réglages.
- **Darks** : images prises sans objectif, avec le capuchon de l'appareil, avec les mêmes réglages que pour les **Images**.<br>
Les **Darks** permettent d'éliminuer le bruit thermique du capteur.
