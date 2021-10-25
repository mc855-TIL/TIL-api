from typing import Any, List

from app.modelo.sqlite.ordem_modelo import Ordem
from app.utils.enums import *
from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.session import Session


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
                Ordem.acao,
                Ordem.item,
                Ordem.nomeInst,
                Ordem.areaConhecimento,
                Ordem.emprestimo,
            )
            .filter(*filtros)
        )

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)

    def visualizar_ordem(
        self,
        id_ordem: int,
    ) -> Row:
        consulta = self.sessao.query(Ordem).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.descricao,
            Ordem.nomeInst,
            Ordem.areaConhecimento,
            Ordem.emprestimo,
            Ordem.data_publicacao,
            Ordem.data_validade,
        )

        return consulta.filter_by(id=id_ordem).one()

    def visualizar_ordem_autenticado(
        self,
        id_ordem: int,
    ) -> Row:

        consulta = self.sessao.query(Ordem).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.descricao,
            Ordem.nomeInst,
            Ordem.areaConhecimento,
            Ordem.emprestimo,
            Ordem.data_publicacao,
            Ordem.data_validade,
            Ordem.contato,
        )
        return consulta.filter_by(id=id_ordem).one()
