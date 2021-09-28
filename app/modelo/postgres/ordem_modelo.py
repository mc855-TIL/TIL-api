import sqlalchemy as sa
from app.config.connection import Base


class Ordem(Base):
    __tablename__ = "ordem"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    titulo = sa.Column(sa.String)
    descricao = sa.Column(sa.String)
    imagem = sa.Column(sa.LargeBinary)
