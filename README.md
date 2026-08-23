# Prédiction de Prix de Voitures d'Occasion 🚗

Projet d'apprentissage du Machine Learning : prédire le prix d'une voiture d'occasion à partir de ses caractéristiques (marque, année, kilométrage, type de carburant, etc.)

## Objectif
Ce projet m'a permis d'apprendre le workflow complet d'un problème de régression en ML :
exploration des données, nettoyage, encodage des variables catégorielles, entraînement
et évaluation de modèles (Linear Regression, Random Forest).

## Étapes réalisées
1. Chargement et exploration des données (`pandas`)
2. Vérification des valeurs manquantes et doublons
3. Encodage one-hot des variables catégorielles (`Brand`, `Fuel Type`, `Transmission`, `Condition`, `Model`)
4. Split train/test (80/20)
5. Entraînement de deux modèles : Linear Regression et Random Forest
6. Évaluation avec MAE et R²

## Résultat et apprentissage clé
Les deux modèles ont obtenu un **R² négatif**, ce qui signifie qu'ils ne trouvent
aucune relation exploitable entre les caractéristiques et le prix. Après analyse,
le dataset source ([Car Price Prediction, Kaggle](https://www.kaggle.com/datasets/zafarali27/car-price-prediction))
semble contenir des prix générés sans corrélation réaliste avec les autres variables
(un modèle plus récent avec moins de kilométrage ne coûte pas nécessairement plus cher).

**Ce que j'en retiens :** un dataset propre (sans valeurs manquantes) n'est pas
forcément un dataset exploitable — il faut aussi vérifier que les données ont un
vrai signal statistique avant
