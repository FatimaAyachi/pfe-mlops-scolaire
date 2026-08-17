# Student Academic Performance Prediction MLOps Pipeline 🎓📊

Ce projet implémente une solution end-to-end pour prédire la réussite académique des étudiants. Il met l'accent sur les bonnes pratiques MLOps, de l'expérimentation au déploiement en conteneurs.

## Architecture Technique
- **Pipeline ML :** Développement et validation de modèles avec `Scikit-Learn`.
- **Suivi MLOps :** Gestion des expériences, versioning des modèles et registre de modèles via `MLflow`.
- **Backend API :** Service d'inférence haute performance construit avec `FastAPI` et `Pydantic`.
- **Interface Utilisateur :** Tableau de bord interactif développé avec `Streamlit`.
- **Conteneurisation & Déploiement :** Docker pour l'isolation, avec déploiement cloud sur Hugging Face Spaces et Streamlit Cloud.

## Stack Technique
- **Language :** Python 3.x
- **Data Science :** Scikit-learn, Pandas, NumPy
- **Serveur API :** FastAPI, Uvicorn
- **Framework UI :** Streamlit
- **MLOps :** MLflow, Docker

## Configuration Docker :

Pour exécuter l'application de manière conteneurisée, utilise les commandes suivantes :

```bash
docker build -t student-performance-app .
docker run -p 8000:8000 student-performance-app
```
## Variables d'environnement
Assure-toi de configurer tes chemins pour le modèle et le registre MLflow comme décrit dans le fichier config.py
## Conseil MLOps :
N'oublie pas d'inclure ton fichier Dockerfile directement à la racine du dépôt. C'est l'un des éléments les plus appréciés par les recruteurs car cela prouve que tu sais rendre tes projets portables et reproductibles dans n'importe quel environnement !
