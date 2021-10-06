from app.modelo.sqlite.ordem_modelo import Ordem
from paginate_sqlalchemy import SqlalchemyOrmPage
from app.api.response.ordem_response import (
    VisualizaOrdemResponse
)
from sqlalchemy import or_
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import or_


class OrdemRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def listar_ordens(
        self,
        pagina: int,
        limite: int,
    ) -> SqlalchemyOrmPage:

        consulta = self.sessao.query(Ordem).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.nomeInst,
            Ordem.areaConhecimento,
            Ordem.emprestimo,
        )

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)

    def buscar_ordens(
        self,
        pesquisa: str,
        pagina: int,
        limite: int,
    ) -> SqlalchemyOrmPage:

        consulta = self.sessao.query(Ordem).with_entities(
            Ordem.id,
            Ordem.acao,
            Ordem.item,
            Ordem.nomeInst,
            Ordem.areaConhecimento,
            Ordem.emprestimo,
        )

        if pesquisa:
            consulta = consulta.filter(
                or_(
                    Ordem.item.ilike(f"%{pesquisa}%"),
                    Ordem.nomeInst.ilike(f"%{pesquisa}%"),
                )
            )

        return SqlalchemyOrmPage(consulta, page=pagina, items_per_page=limite)


    def visualizar_ordem(
        self,
        id_ordem: int,
        auth: bool,
    ) -> VisualizaOrdemResponse:

        if auth:
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
                Ordem.contato
            )
            consulta = consulta.filter_by(id=id_ordem)
            ordem = consulta.one()
            print(' Ordem = ', ordem)
            print(type(consulta))
            # print (response)
            response = VisualizaOrdemResponse(
                id = ordem[0],
                acao = ordem[1],
                item = ordem[2],
                descricao = ordem[3],
                nomeInst = ordem[4],
                areaConhecimento = ordem[5],
                emprestimo = ordem[6],
                dataPublicacao = ordem[7],
                dataValidade = ordem[8],
                contato = ordem[9]
            )
        else:
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
            consulta = consulta.filter_by(id=id_ordem)
            ordem = consulta.one()


            response = VisualizaOrdemResponse(
                id = ordem[0],
                acao = ordem[1],
                item = ordem[2],
                descricao = ordem[3],
                nomeInst = ordem[4],
                areaConhecimento = ordem[5],
                emprestimo = ordem[6],
                dataPublicacao = ordem[7],
                dataValidade = ordem[8],
            )
        return response