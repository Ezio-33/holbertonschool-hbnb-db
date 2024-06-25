""" Entry point for the application. """

from src import db, create_app
from src.persistence import FileRepository
from flask.cli import FlaskGroup


app = create_app()
cli = FlaskGroup(create_app=create_app)


class DataManager:
    def save_user(self, user):
        if app.config['USE_DATABASE']:
            db.session.add(user)
            db.session.commit()
        else:
            file_repository = FileRepository()
            file_repository._save_to_file(data=user)


@app.cli.command("init_db")
def init_db():
    """ Initialize the database. """
    with app.app_context():
        db.create_all()
        print("Database initialized.")


if __name__ == "__main__":
    cli()
