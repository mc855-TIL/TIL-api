import sqlalchemy as sa
from app.config.conexao import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    nome = sa.Column(sa.String)
    email = sa.Column(sa.String)
    contato = sa.Column(sa.String)
    id_inst = sa.Column(sa.Integer, sa.ForeignKey("instituicao.id"), nullable=False)
