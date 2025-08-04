# 📉 Suivi Poids & Mesures

Webapp Streamlit pour suivre l’évolution du poids, du tour de taille et du tour de poitrine avec base de données SQLite.

## Fonctionnalités

- Ajout manuel des mesures avec choix de la date
- Calculs :
  - Moyenne glissante sur 7 jours
  - Moyenne hebdomadaire fixe
  - Tendance linéaire
  - Courbe d’objectif pondéral
- Visualisations interactives

## Démarrage

```bash
pip install -r requirements.txt
streamlit run main.py
