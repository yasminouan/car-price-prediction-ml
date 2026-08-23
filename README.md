# Prédiction de Prix de Voitures d'Occasion 🚗

Projet d'apprentissage du Machine Learning : prédire le prix de revente d'une voiture
d'occasion à partir de ses caractéristiques (année, kilométrage, carburant, etc.)

## Objectif
Ce projet m'a permis d'apprendre le workflow complet d'un problème de régression en ML :
exploration des données, nettoyage, encodage des variables catégorielles, entraînement
et évaluation de modèles.

## Étapes réalisées
1. Chargement et exploration des données (`pandas`)
2. Nettoyage : suppression des valeurs manquantes, extraction des valeurs numériques
   depuis des colonnes texte (ex: "23.4 kmpl" → 23.4)
3. Encodage one-hot des variables catégorielles (`fuel`, `seller_type`, `transmission`, `owner`)
4. Split train/test (80/20)
5. Entraînement d'un modèle Random Forest
6. Évaluation avec MAE et R²
7. Sauvegarde du modèle entraîné (`joblib`)

## Résultat
**R² = 0.98** — le modèle explique 98% des variations de prix de vente.
**MAE ≈ 61 000** (erreur moyenne, à l'échelle des prix qui vont jusqu'à plusieurs millions).

## Note méthodologique
Une première tentative avec un autre dataset Kaggle a donné un R² négatif : les prix
de ce dataset étaient générés sans corrélation réaliste avec les autres variables.
Ça m'a appris qu'un dataset propre (sans valeurs manquantes) n'est pas forcément
exploitable — il faut aussi vérifier qu'il contient un vrai signal statistique
avant d'investir du temps dans la modélisation.

## Données
[Vehicle dataset (CarDekho), Kaggle](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)

## Stack
Python, pandas, scikit-learn, Google Colab
