# Solution HBNB Partie 1

Cette solution implémente avec succès le modèle de dépôt.
Elle passe les tests fournis dans le répertoire `/hbnb/part1/tests`.

## Quelques points à noter

- N'implémente pas encore les `endpoints` place_amenities.
- Les dépôts implémentés sont `FileRepository` et `MemoryRepository`, et il y a également un espace réservé pour un `DBRepository`.
- Le `MemoryRepository` ne persiste pas les données entre les exécutions.
- Le `FileRepository` persiste les données dans un fichier JSON par défaut appelé `data.json`.
- Il a été conçu au départ pour fonctionner avec la mémoire uniquement pour tester les tests.

## Que devez-vous savoir sur la solution ?

- Les dépôts ont une classe de base appelée Repository qui contient les méthodes que les dépôts doivent implémenter. La classe elle-même est une classe abstraite, et toutes les méthodes sont des méthodes abstraites.
  - Les méthodes sont : `get`, `get_all`, `reload`, `save`, `update`, `delete`.
- Les modèles ont une classe de base appelée Base qui est une classe abstraite, elle contient trois types de méthodes :
  - @abstractmethods - méthodes que la classe qui hérite de Base doit implémenter. Les méthodes sont : `to_dict`
  - @classmethods - Ces méthodes sont : `get`, `get_all`, `delete`. La logique de ces méthodes est la même pour tous les modèles, donc elle a été implémentée dans la classe Base.
  - @staticabstractmethods - méthodes que la classe qui hérite de Base doit implémenter, mais sont des méthodes statiques. Les méthodes sont : `create`, `update`.

Il n'y a pas encore de documentation. **_Et rien ici n'a été créé avec ChatGPT_**. Désolé si quelque chose n'est pas assez clair 😅. N'hésitez pas à me contacter si vous ne comprenez pas quelque chose, je suis _Ignacio Peralta_ trouvez-moi sur Slack.

> [!TIP]
> Vous pouvez précharger la couche de persistance sélectionnée via la méthode `reload` dans la classe `Repository`.
> Cette méthode est appelée dans la méthode `__init__` de la classe `Repository`.

---

> [!IMPORTANT]
> Les tests ne passeront pas s'il n'y a pas un pays fictif créé, par exemple `MemoryRepository` dans la fonction reload crée un pays fictif `UY` via la méthode `reload` qui appelle également la fonction `populate_db` dans le fichier `utils/populate.py`.

## MVC

La solution est divisée en quatre parties principales : `Models`, `Controllers`, et `Persistence`, mais n'utilise pas de Vues car il s'agit simplement d'une API REST.

- Dans le package `controllers`, vous trouverez la logique pour les endpoints de l'API.
- Dans le package `models`, vous trouverez les classes qui représentent les données.
- Dans le package `routes`, vous trouverez les routes pour l'API, qui sont des routes qui appellent les contrôleurs.
- Dans le package `persistence`, vous trouverez les dépôts qui gèrent les données.

## Comment fonctionne la solution ?

L'application est construite en utilisant le modèle de fabrique. La fonction `create_app` dans le fichier `src/__init__.py` crée l'application et la retourne. La fonction accepte un objet `config` qui est utilisé pour configurer l'application. Elle enregistre les routes, les gestionnaires d'erreurs, cors, puis retourne l'application.

Pour exécuter l'application, vous pouvez simplement exécuter l'objet app retourné par la fonction `create_app` comme le fait le fichier `hbnb.py`. Ou vous pouvez exécuter le fichier `manage.py`, qui utilise le `Flask CLI`, avec `python manage.py run` pour exécuter l'application.

Les routes sont divisées en `Blueprints` et sont enregistrées dans la fonction `create_app` mentionnée ci-dessus. Les routes sont situées dans le répertoire `src/routes`.

Les routes définies dans les fichiers utilisent les contrôleurs pour gérer les requêtes. Les contrôleurs sont dans le répertoire `src/controllers`.

Ensuite, les contrôleurs interrogent les modèles pour récupérer ou enregistrer les données. Les modèles sont dans le répertoire `src/models`.

Et les modèles utilisent le dépôt sélectionné actuel pour gérer les données. Les dépôts sont dans le répertoire `src/persistence`. Le fichier `src/persistence/__init__.py` exporte un objet `db` qui est le dépôt sélectionné actuel.

Donc, le flux est comme ceci :

```text
Requête -> Route -> Contrôleur -> Modèle -> Dépôt
(puis tout le chemin de retour)
Réponse <- Route <- Contrôleur <- Modèle <- Dépôt
```

Vous pouvez choisir le dépôt que vous souhaitez utiliser en définissant la variable d'environnement `REPOSITORY_TYPE` sur `memory`, `file`, ou `db`. La valeur par défaut est `memory`.

---

Juste pour mentionner, il y a un package `utils` qui pour l'instant contient seulement deux fichiers, `constants.py` et `populate.py`. Le fichier `constants.py` contient les constantes utilisées dans l'application, et le fichier `populate.py` contient la logique pour peupler la base de données avec certaines données.

Vous pouvez changer les constantes arbitrairement.

## Comment exécuter

Pour exécuter la solution, installez d'abord les dépendances avec `pip install -r requirements.txt`. Ensuite, il y a plusieurs façons de l'exécuter :

- Exécutez le fichier `manage.py` avec la commande `python manage.py run` et spécifiez des options comme `--port {port} --host {host}` si vous souhaitez l'exécuter sur un port ou un hôte différent.
- Exécutez le fichier `hbnb.py`. Ce fichier appelle une fonction avant d'exécuter l'application qui peuplera la base de données avec certaines données.
- Construisez et exécutez le Dockerfile.
