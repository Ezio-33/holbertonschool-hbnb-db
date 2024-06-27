""" Entry point for the application. """

from flask.cli import FlaskGroup
from src import create_app
from src.persistence import db


app = create_app()
cli = FlaskGroup(create_app=create_app)


class DataManager:
    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(user)

    def save_amenity(self, amenity):
        if app.config['USE_DATABASE']:
            db.session.add(amenity)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(amenity)

    def save_place(self, place):
        if app.config['USE_DATABASE']:
            db.session.add(place)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(place)

    def save_review(self, review):
        if app.config['USE_DATABASE']:
            db.session.add(review)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(review)

    def save_country(self, country):
        if app.config['USE_DATABASE']:
            db.session.add(country)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(country)

    def save_city(self, city):
        if app.config['USE_DATABASE']:
            db.session.add(city)
            db.session.commit()
        else:
            from src.persistence.file import FileRepository
            file_repository = FileRepository()
            file_repository._save_to_file(city)


@app.cli.command("init_db")
def init_db():
    """ Initialize the database. """
    with app.app_context():
        db.create_all()
        print("Database initialized.")


if __name__ == "__main__":
    cli()
