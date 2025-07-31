import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "clave-supersecreta")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    DEBUG = False
