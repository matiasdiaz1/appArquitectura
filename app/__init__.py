# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializamos la base de datos y migraciones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Puedes cambiar la URI si usas otra base de datos
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializamos la base de datos y migraciones
    db.init_app(app)
    migrate.init_app(app, db)

    # Ruta raíz para pruebas
    @app.route('/')
    def home():
        return 'Welcome to the API!'

    # Importamos y registramos los blueprints
    from views.UserView import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api')

    # Importamos los modelos aquí (asegúrate de que el nombre del archivo coincida con el del modelo)
    from models.UserModel import User
    from models.TaskModel import Task

    return app
