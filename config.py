import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jakeh1001hc'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///mi-base-de-datos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False