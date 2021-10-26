from typing import Any, List

from app.modelo.sqlite.ordem_modelo import Ordem
from app.modelo.sqlite.usuario_modelo import Usuario
from app.modelo.sqlite.instituicao_modelo import Instituicao
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
            self.sessao.query(Ordem).join(Usuario).join(Instituicao)
            .with_entities(
                Ordem.id,
                Ordem.acao,
                Ordem.item,
                Instituicao.nome.label('nome_instituicao'),
                Ordem.area_conhecimento,
                Ordem.emprestimo,
            )
            .filter(*filtros)
        )

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)

    def visualizar_ordem(
        self,
        id_ordem: int,
    ) -> Row:
        consulta = self.sessao.query(Ordem).join(Usuario).join(Instituicao).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.descricao,
            Ordem.area_conhecimento,
            Ordem.emprestimo,
            Ordem.data_publicacao,
            Ordem.data_validade,
            Instituicao.nome.label('nome_instituicao'),
        )

        return consulta.filter_by(id=id_ordem).one()

    def visualizar_ordem_autenticado(
        self,
        id_ordem: int,
    ) -> Row:

        consulta = self.sessao.query(Ordem).join(Usuario).join(Instituicao).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.descricao,
            Ordem.area_conhecimento,
            Ordem.emprestimo,
            Ordem.data_publicacao,
            Ordem.data_validade,
            Usuario.contato,
            Ordem.quantidade,
            Instituicao.nome.label('nome_instituicao'),
        )
        return consulta.filter_by(id=id_ordem).one()
