from typing import Any, List

from app.modelo.sqlite.ordem_modelo import Ordem
from app.utils.enums import *
from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy import or_
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import or_


class OrdemRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def listar_ordens(
        self,
        filtros: List[Any],
        pagina: int,
        limite: int,
    ) -> SqlalchemyOrmPage:

        consulta = (
            self.sessao.query(Ordem)
            .with_entities(
                Ordem.id,
                Ordem.tipo,
                Ordem.item,
                Ordem.nomeInst,
                Ordem.areaConhecimento,
                Ordem.emprestimo,
            )
            .filter(*filtros)
        )

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)
