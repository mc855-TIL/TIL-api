from typing import Any, List

from app.modelo.sqlite.instituicao_modelo import Instituicao
from app.modelo.sqlite.negocio_modelo import Negocio
from app.modelo.sqlite.ordem_modelo import Ordem
from app.modelo.sqlite.usuario_modelo import Usuario
from app.utils.enums import *
from paginate_sqlalchemy import SqlalchemyOrmPage
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.row import Row


class NegocioRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def criar_negocio(
        self,
        negocio: Negocio,
    ) -> None:
        with self.sessao.begin():
            self.sessao.merge(negocio)

            # parametros = {"status": StatusOrdemEnum.EM_NEGOCIACAO.value
            # }
            # consulta = (self.sessao.query(Ordem))
            # consulta.filter_by(id=negocio.id_ordem) \
            # .update(parametros)

    def listar_negocios(
        self,
        filtros: List[Any]
    ) -> List[Row]:

        consulta = (
            self.sessao.query(Negocio)
            .join(Usuario)
            .join(Instituicao)
            .with_entities(
                Negocio.id,
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
            consulta = (
                self.sessao.query(Negocio)
            )
            consulta.filter_by(id_ordem=id_ordem).delete()


    def deletar_negocio(
        self,
        id_negocio: int,
    ) -> None:
        with self.sessao.begin():
            consulta = (
                self.sessao.query(Negocio)
            )
            consulta.filter_by(id=id_negocio).delete()

    def atualiza_ordem(
        self,
        negocio: Negocio,
    ) -> None:

        parametros_nomes = [
            "id",
            "status",
            "data_hora_resposta",
        ]
        parametros_nao_nulos = {p: getattr(negocio, p, None)
                                for p in parametros_nomes
                                if getattr(negocio, p, None)
        }
        print(parametros_nao_nulos)
        with self.sessao.begin():
            consulta = (self.sessao.query(Negocio))

            consulta.filter_by(id=negocio.id) \
            .update(parametros_nao_nulos)

            consulta = (self.sessao.query(Negocio))

            negres = consulta.filter_by(id=negocio.id) \
            .one()
            id_ordem = negres.id_ordem

            parametros = {"status": StatusOrdemEnum.FINALIZADO.value
            }
            consulta = (self.sessao.query(Ordem))
            consulta.filter_by(id=id_ordem) \
            .update(parametros)


