import sqlalchemy as sa
from app.config.conexao import Base


class Instituicao(Base):
    __tablename__ = "instituicao"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    nome = sa.Column(sa.String)
    endereco = sa.Column(sa.String)
