from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa o Flask-Migrate

db = SQLAlchemy()
migrate = Migrate()  # Cria uma instância de Migrate

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta-super-segura'  # Adicione essa linha
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)  # Inicializa o Flask-Migrate com a aplicação e o banco de dados

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app