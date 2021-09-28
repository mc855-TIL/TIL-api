import sqlalchemy as sa
from app.config.connection import Base


class Ordem(Base):
    __tablename__ = "ordem"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    item = sa.Column(sa.String)
    descricao = sa.Column(sa.String, nullable=True)
    acao = sa.Column(sa.String)
    tipo = sa.Column(sa.String)
    data_publicacao = sa.Column(sa.Date)
    data_validade = sa.Column(sa.Date, nullable=True)
    nomeInst = sa.Column(sa.Date)
    emprestimo = sa.Column(sa.Boolean)
