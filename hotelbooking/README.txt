



Application de réservation de chambre d'hotel faite avec le Framework Django



<img src="https://i.ibb.co/m6Ss4gF/HomePage.png"/>


### Fonctionnalités
1. Les utilisateurs peuvent créer leur compte utilisateur.
2. Les utilisateurs peuvent se connecter pour pouvoir réserver leurs chambres.
3. Les utilisateurs peuvent voir les différents types de chambre qu'il y a dans l'hotel.
4. Les utilisateurs peuvent réserver leurs chambres d'hotel.



### Fichiers et répertoires
   - `hotelbooking` - répertoire du projet.
     - `urls.py` - Ce fichier gère toutes les URL du projet.
   - `booking` - répertoire principal de l'application.
     - `static` - contient tout le contenu statique.
         - `css` - Contient tous les fichiers CSS pour styliser les pages Web.
         - `js` - Contient tous les fichiers javascript utilisés dans l'application.
         - `img` - Contient tous les fichiers image utilisés dans l'application.
     - `booking/templates` Contient tous les modèles d'application.
         - `rooms.html` - Modèle pour afficher les différentes chambres disponible dans l'entrprise.
         - `index.html` - Modèle de page d'accueil.
         - `reservation.html` - Modèle de formulaire pour réserver une chambre d'hotel.
         - `login.html` - Page utilisateur de connexion.
         - `register.html` - Page d'enregistrement de l'utilisateur.
     - `admin.py` - Contient quelques modèles pour l'accès à l'administrateur Django.
     - `models.py` - Tous les modèles utilisés dans l'application sont créés ici.
     - `urls.py` - Ce fichier gère toutes les URL de l'application Web.
     - `views.py` - Ce fichier contient toutes les vues de l'application.
     - `constant.py` - Ce fichier contient le montant des frais facturés à l'utilisateur pour la réservation de billets d'avion.
   - `requirements.txt` - Ce fichier contient tous les packages python qui doivent être installés pour exécuter cette application Web.
   - `manage.py` - Ce fichier est essentiellement utilisé comme utilitaire de ligne de commande et pour déployer, déboguer ou exécuter notre application Web.


### Installation

- Activez l'environnement virtuel en exécutant `. .\env\Scripts\activate`
- Installez les dépendances du projet en exécutant `py -m pip install -r requirements.txt`.
- Créez un superutilisateur avec `py manage.py createsuperuser`. Cette étape est facultative.
- Exécutez la commande `py manage.py runserver` pour exécuter le serveur Web.
- Ouvrez le navigateur Web et accédez à l'URL `127.0.0.1:8000` pour commencer à utiliser l'application Web.
