import sys
import os
import pytest
from flask import Flask
from src import create_app
from src.persistence import db
from src.models.user import User
from src.models.place import Place
from src.models.city import City
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(app):
    user_data = {
        'email': 'test@example.com',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    }
    with app.app_context():
        user = User.create(user_data)
        assert user.id is not None
        assert user.email == 'test@example.com'

def test_create_place(app):
    user_data = {
        'email': 'host@example.com',
        'password': 'password123',
        'first_name': 'Host',
        'last_name': 'User'
    }
    city_data = {
        'id': 'city1',
        'name': 'Test City'
    }
    with app.app_context():
        user = User.create(user_data)
        city = City(**city_data)
        db.session.add(city)
        db.session.commit()

        place_data = {
            'name': 'Test Place',
            'description': 'A nice place',
            'address': '123 Main St',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'host_id': user.id,
            'city_id': city.id,
            'price_per_night': 100,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'max_guests': 4
        }
        place = Place.create(place_data)
        assert place.id is not None
        assert place.name == 'Test Place'
