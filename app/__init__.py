from flask import Flask

from config import load_config

config = load_config('.env')

# app = Flask(__name__)
# app.config.from_object(Config)


# from app import routes
