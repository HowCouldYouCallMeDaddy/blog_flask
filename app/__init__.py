from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .main import main
    app.register_blueprint(main)
    return app

