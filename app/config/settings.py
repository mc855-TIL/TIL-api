import os
from distutils.util import strtobool

from pydantic import BaseSettings


class Base(BaseSettings):
    # limite de dados por pagina
    QUANTIDADE_PAGINA: int = 20

    # database info
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_URL: str
    DATABASE_DBNAME: str
    SQLALCHEMY_DATABASE_URL: str
    SQLALCHEMY_ECHO: str


class DevSettings(Base):
    ENVIRONMENT: str = "dev"


class PrdSettings(Base):
    ENVIRONMENT: str = "prd"


def get_settings(env: str) -> Base:
    envs = {
        "dev": DevSettings(),
        "prd": PrdSettings(),
    }
    return envs[env]


settings = get_settings(env=os.getenv("ENVIRONMENT", "dev"))
