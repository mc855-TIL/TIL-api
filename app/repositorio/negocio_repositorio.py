from typing import Any, List

from app.modelo.sqlite.instituicao_modelo import Instituicao
from app.modelo.sqlite.negocio_modelo import Negocio
from app.modelo.sqlite.ordem_modelo import Ordem
from app.modelo.sqlite.usuario_modelo import Usuario
from app.utils.enums import *
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.session import Session


class NegocioRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def criar_negocio(
        self,
        negocio: Negocio,
    ) -> None:
        with self.sessao.begin():
            self.sessao.merge(negocio)

    def listar_negocios(self, filtros: List[Any]) -> List[Row]:

        consulta = (
            self.sessao.query(Negocio)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
                Negocio.id,
                Negocio.status,
                Usuario.nome.label("nome_solicitante"),
                Instituicao.nome.label("nome_instituicao"),
            )
            .filter(*filtros)
        )

        res = consulta.distinct().all()
        return res

    def deletar_todos_negocios_ordem(
        self,
        id_ordem: int,
    ) -> None:
        with self.sessao.begin():
            consulta = self.sessao.query(Negocio)
            consulta.filter_by(id_ordem=id_ordem).delete()

    def deletar_negocio(
        self,
        id_negocio: int,
    ) -> None:
        with self.sessao.begin():
            consulta = self.sessao.query(Negocio)
            consulta.filter_by(id=id_negocio).delete()

    def atualiza_negocio(
        self,
        negocio: Negocio,
    ) -> None:

        parametros_nomes = [
            "id",
            "status",
            "data_hora_resposta",
        ]
        parametros_nao_nulos = {
            p: getattr(negocio, p, None)
            for p in parametros_nomes
            if getattr(negocio, p, None)
        }

        with self.sessao.begin():
            consulta = self.sessao.query(Negocio)

            consulta.filter_by(id=negocio.id).update(parametros_nao_nulos)

    def listar_todas_solicitacoes(
        self,
        filtros: List[Any],
    )->List[Row]:

        consulta = (
            self.sessao.query(Negocio)
            .join(Ordem)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
                Negocio.id,
                Negocio.status,
                Ordem.item.label("nome_ordem"),
                Instituicao.nome.label("nome_instituicao"),
            )
            .filter(*filtros)
        )

        res = consulta.distinct().all()
        return res
