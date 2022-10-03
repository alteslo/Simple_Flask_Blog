from dataclasses import dataclass
from environs import Env


@dataclass
class FlaskConfig:
    secret_key: str


@dataclass
class Config:
    flask: FlaskConfig


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        flask=FlaskConfig(
            secret_key=env.str('SECRET_KEY')
        )
    )
