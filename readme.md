# Django Web App - Merchex

## Description du projet
Merchex est une application qui permet de gérer et d'afficher des informations sur des groupes de musique ainsi que des annonces de vente de merchandises liées à ces groupes. Les utilisateurs peuvent consulter les détails des groupes, leurs biographies, et parcourir des annonces pour acheter des disques, vêtements, posters ou autres objets musicaux.

L'application inclut des fonctionnalités de base telles que :
- Liste des groupes de musique
- Détails des groupes (genre, année de formation, biographie, site officiel)
- Annonces de vente (listings) avec titre, description, type d'objet, année, et statut de vente
- Pages statiques (à propos, contact)

## Technologies utilisées
- **Langage** : `Python`
- **Framework web** : `Django` (version 6.0.4)
- **Base de données** : `SQLite` (par défaut de Django)
- **Templates** : `Django Templates`
- **Styles** : `CSS`
- **Environnement** : Virtualenv (dossier `env/`)
- **Gestion des dépendances** : `pip` (fichier `requirements.txt`)

## Installation et exécution
1. Activer l'environnement virtuel :
   ```
   source env/bin/activate  # Sur Linux/Mac
   # ou env\Scripts\activate sur Windows
   ```

2. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

3. Appliquer les migrations de base de données :
   ```
   cd merchex
   python manage.py migrate
   ```

4. Lancer le serveur de développement :
   ```
   python manage.py runserver
   ```

5. Accéder à l'application dans un navigateur : `http://127.0.0.1:8000/`

## Structure du projet
- `merchex/` : Projet Django principal
  - `listing/` : Application Django pour la gestion des bands et listings
  - `db.sqlite3` : Base de données SQLite
  - `manage.py` : Script de gestion Django
- `env/` : Environnement virtuel Python
- `requirements.txt` : Dépendances Python

## Auteur
- Maxime Cordier