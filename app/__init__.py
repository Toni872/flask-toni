from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from recommender import CocktailRecommender

# Crear la aplicación Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# Inicializar las extensiones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

# Crear una instancia de CocktailRecommender dentro del contexto de la aplicación Flask
with app.app_context():
    cocktailRecommender = CocktailRecommender(
        taxonomy_file="data/taxonomy_taste.csv",
        cocktail_file="data/ccc_cocktails.xml",
        general_taxonomy_file="data/general_taxonomy.csv"
    )

# Importar las rutas de la aplicación
from app import routes
