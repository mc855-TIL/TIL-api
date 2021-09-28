from typing import List

from app.modelo.postgres.ordem_modelo import Ordem
from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy.orm.session import Session


class OrdemRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def listar_ordens(
        self,
    ) -> SqlalchemyOrmPage:
        consulta = self.sessao.query(Ordem).all()
        pass

    def buscar_ordens(
        self,
    ) -> SqlalchemyOrmPage:
        consulta = self.sessao.query(Ordem).all()

        pass
