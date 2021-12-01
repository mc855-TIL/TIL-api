from typing import Any, List

from app.modelo.sqlite.instituicao_modelo import Instituicao
from app.modelo.sqlite.negocio_modelo import Negocio
from app.modelo.sqlite.ordem_modelo import Ordem
from app.modelo.sqlite.usuario_modelo import Usuario
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
        ultimos: bool,
        pagina: int,
        limite: int,
    ) -> SqlalchemyOrmPage:

        consulta = (
            self.sessao.query(Ordem)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
                Ordem.id,
                Ordem.acao,
                Ordem.item,
                Instituicao.nome.label("nome_instituicao"),
                Ordem.area_conhecimento,
                Ordem.emprestimo,
            )
            .filter(*filtros)
        )

        if ultimos:
            consulta = consulta.order_by(Ordem.data_publicacao.desc())

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)

    def visualizar_ordem(
        self,
        id_ordem: int,
    ) -> Ordem:
        consulta = (
            self.sessao.query(Ordem)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
                Ordem.id,
                Ordem.acao,
                Ordem.item,
                Ordem.descricao,
                Ordem.area_conhecimento,
                Ordem.emprestimo,
                Ordem.data_publicacao,
                Ordem.data_validade,
                Ordem.quantidade,
                Instituicao.nome.label("nome_instituicao"),
            )
        )

        return consulta.filter_by(id=id_ordem).one()

    def visualizar_ordem_autenticado(
        self,
        id_ordem: int,
    ) -> Ordem:
        consulta = (
            self.sessao.query(Ordem)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
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
                Instituicao.nome.label("nome_instituicao"),
            )
        )
        return consulta.filter_by(id=id_ordem).one()

    def criar_ordem(
        self,
        ordem: Ordem,
    ) -> None:
        with self.sessao.transaction:
            self.sessao.merge(ordem)

    def pesquisar_nome_item(
        self,
        filtros: List[Any],
    ) -> List[Row]:

        consulta = (
            self.sessao.query(Ordem)
            .with_entities(
                Ordem.item,
            )
            .filter(*filtros)
        )

        res = consulta.distinct().all()
        return res

    def deletar_ordem(
        self,
        id_ordem: int,
    ) -> None:
        with self.sessao.begin():
            consulta = self.sessao.query(Ordem)
            consulta.filter_by(id=id_ordem).delete()

    def atualiza_ordem(
        self,
        ordem: Ordem,
    ) -> None:

        parametros_nomes = [
            "id",
            "item",
            "descricao",
            "tipo",
            "data_validade",
            "emprestimo",
            "quantidade",
            "id_usuario",
        ]
        parametros_nao_nulos = {p: getattr(ordem, p, None) for p in parametros_nomes if getattr(ordem, p, None)}
        with self.sessao.begin():
            consulta = self.sessao.query(Ordem)

            consulta.filter_by(id=ordem.id).update(parametros_nao_nulos)

    def atualiza_ordem_status(
        self,
        id_negocio,
    ):
        consulta = self.sessao.query(Negocio)

        negocio = consulta.filter_by(id=id_negocio).one()
        id_ordem = negocio.id_ordem

        parametros = {"status": StatusOrdemEnum.FINALIZADO.value}
        consulta = self.sessao.query(Ordem)
        consulta.filter_by(id=id_ordem).update(parametros)
