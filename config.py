import os
from environs import Env

env = Env()
print('-----------Читаем файл .env------------')
basedir = os.path.abspath(os.path.dirname(__file__))
env.read_env(os.path.join(basedir, '.env'))


class BaseConfig:
    SECRET_KEY = env.str('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = env.str('MAIL_SERVER')
    MAIL_PORT = env.int('MAIL_PORT')
    MAIL_USE_TLS = env.int('MAIL_USE_TLS')
    MAIL_USERNAME = env.str('MAIL_USERNAME')
    MAIL_PASSWORD = env.str('MAIL_PASSWORD')
    ADMINS = env.list('ADMINS')


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
