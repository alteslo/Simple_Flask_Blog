import os
from environs import Env

env = Env()
env.read_env()
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = env.str(name='SECRET_KEY', default='easy_key')
    SQLALCHEMY_DATABASE_URI = env.str(
        name='DATABASE_URL',
        default='///'.join(['sqlite:', os.path.join(basedir, 'app.db')])
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = env.str('MAIL_SERVER')
    MAIL_PORT = env.int('MAIL_PORT')
    MAIL_USE_TLS = env.int('MAIL_USE_TLS')
    MAIL_USERNAME = env.str('MAIL_USERNAME')
    MAIL_PASSWORD = env.str('MAIL_PASSWORD')
    ADMINS = env.list('ADMINS')


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
