import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance.config import Config
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'Img-prop')  # Configura la carpeta de subidas


    db.init_app(app)

    # Crear las tablas si no existen
    with app.app_context():
        db.create_all()

    # Registrar el blueprint de rutas
    from .routes import main
    app.register_blueprint(main)


    return app