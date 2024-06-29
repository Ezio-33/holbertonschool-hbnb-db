""" Initialize the Flask app. """

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from src.models import User  # Assurez-vous d'importer votre modèle User depuis le bon chemin
import secrets

db = SQLAlchemy()
cors = CORS()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app() -> Flask:
    """
    Créer une application Flask avec la classe de configuration donnée.
    La classe de configuration par défaut est DevelopmentConfig.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Générer une clé aléatoire sécurisée pour JWT_SECRET_KEY
    jwt_secret_key = secrets.token_urlsafe(32)
    app.config['JWT_SECRET_KEY'] = jwt_secret_key

    register_extensions(app)
    register_routes(app)
    register_handlers(app)

    return app

def register_extensions(app: Flask) -> None:
    """Enregistrer les extensions pour l'application Flask"""
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

def register_routes(app: Flask) -> None:
    """Importer et enregistrer les routes pour l'application Flask"""
    from src.routes.users import users_bp
    from src.routes.countries import countries_bp
    from src.routes.cities import cities_bp
    from src.routes.places import places_bp
    from src.routes.amenities import amenities_bp
    from src.routes.reviews import reviews_bp
    from src.routes.auth import auth_bp  

    # Enregistrer les blueprints dans l'application
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(amenities_bp)
    app.register_blueprint(auth_bp)  

def register_handlers(app: Flask) -> None:
    """Register the error handlers for the Flask app."""
    app.errorhandler(404)(lambda e: (
        {"error": "Not found", "message": str(e)}, 404
    )
    )
    app.errorhandler(400)(
        lambda e: (
            {"error": "Bad request", "message": str(e)}, 400
        )
    )

# Importez et configurez les routes d'authentification dans un nouveau fichier src/routes/auth.py

# Exemple de contenu pour src/routes/auth.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.models import User
from src import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Requête JSON requise"}), 400

    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email or not password:
        return jsonify({"msg": "Identifiant ou mot de passe manquant"}), 400

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"msg": "Identifiant ou mot de passe incorrect"}), 401

    access_token = create_access_token(identity=user.email)
    return jsonify(access_token=access_token), 200

# Exemple de sécurisation d'un endpoint avec JWT
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200