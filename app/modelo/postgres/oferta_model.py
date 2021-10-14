import sqlalchemy as sa
from app.config.connection import Base


class Oferta(Base):
    __tablename__ = "oferta"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    titulo = sa.Column(sa.String)
    descricao = sa.Column(sa.String)
    imagem = sa.Column(sa.LargeBinary)
