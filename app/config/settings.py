import os
from distutils.util import strtobool
from pathlib import Path
from urllib.parse import quote

from pydantic import BaseSettings

root_path = str(Path(__file__).parent.parent.parent)


class Base(BaseSettings):
    # limite de dados por pagina
    QUANTIDADE_PAGINA: int = 20

    # database info
    # DATABASE_USERNAME: str = quote(os.environ["DATABASE_USERNAME"])
    # DATABASE_PASSWORD: str = quote(os.environ["DATABASE_PASSWORD"])
    # DATABASE_URL: str = os.environ["DATABASE_URL"]
    # DATABASE_DBNAME: str = os.environ["DATABASE_DBNAME"]
    # SQLALCHEMY_ECHO: bool = strtobool(os.getenv("SQLALCHEMY_ECHO", "false"))

    SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{root_path}/database.db"
    SQLALCHEMY_ECHO: bool = True


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
