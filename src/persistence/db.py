"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from sqlalchemy.orm import session
from src.models.base import Base
from src.persistence.repository import Repository
from src import db


class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self, session) -> None:
        """ Configuration de la base de données SQLite. """
        self.session = session

    def get_all(self, model_name: str) -> list:
        """Récupère tous les objets d'un modèle spécifié depuis la base de données"""
        model_class = self.get(model_name)

        if not model_class:
            raise ValueError(f"Model '{model_name}' is not found.")

        try:
            return db.session.query(model_class).all()
        except:
            return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Récupère un objet spécifique par son identifiant depuis la base de données"""
        model_class = self.get(model_name, obj_id)

        if not model_class:
            raise ValueError(f"Model '{model_name}' is not found.")

        return db.session.query(model_class).get(obj_id)

    def reload(self):
        """Recharge les données ou actualise l'état de l'objet"""
        pass

    def save(self, obj: Base) -> None:
        """ Sauvegarde un nouvel objet dans la base de données. """
        self.session.add(obj)
        self.session.commit()

    def update(self, obj: Base) -> Base | None:
        """Met à jour un objet existant dans la base de données"""
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete(self, obj: Base) -> bool:
        """Supprime un objet de la base de données"""
        try:
            self.session.delete(obj)
            self.session.commit()
            return True
        except:
            return False
