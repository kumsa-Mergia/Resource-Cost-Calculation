from dotenv import load_dotenv
load_dotenv()
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cooperative_bank_of_oromia')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
