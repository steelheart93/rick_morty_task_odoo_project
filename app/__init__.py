from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_app.db'

    db.init_app(app)
    login_manager.init_app(app)

    from .routes.auth import auth_bp
    from .routes.tasks import tasks_bp
    from .routes.characters import characters_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(characters_bp)

    with app.app_context():
        db.create_all()

    return app
