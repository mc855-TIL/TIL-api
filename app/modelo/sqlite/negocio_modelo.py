import sqlalchemy as sa
from app.config.conexao import Base


class Negocio(Base):
    __tablename__ = "negocio"

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    id_ordem = sa.Column(
        sa.Integer,
        sa.ForeignKey("ordem.id"),
        nullable=False,
    )
    id_solicitante = sa.Column(
        sa.Integer,
        sa.ForeignKey("usuario.id"),
        nullable=False,
    )
    status = sa.Column(sa.String)
    data_hora_criacao = sa.Column(sa.DateTime)
    data_hora_resposta = sa.Column(sa.DateTime)
