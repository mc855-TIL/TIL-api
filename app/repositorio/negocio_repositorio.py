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

            parametros = {"status": StatusOrdemEnum.EM_NEGOCIACAO.value
            }


            consulta = (self.sessao.query(Ordem))

            consulta.filter_by(id=negocio.id_ordem) \
            .update(parametros)

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
