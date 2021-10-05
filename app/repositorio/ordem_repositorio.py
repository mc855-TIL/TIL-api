from app.modelo.sqlite.ordem_modelo import Ordem
from paginate_sqlalchemy import SqlalchemyOrmPage
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
            Ordem.tipo,
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
            Ordem.tipo,
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
    ) -> SqlalchemyOrmPage:

        consulta = self.sessao.query(Ordem).with_entities(
            Ordem.id,
            Ordem.tipo,
            Ordem.item,
            Ordem.nomeInst,
            Ordem.areaConhecimento,
            Ordem.emprestimo,
        )
        consulta = consulta.filter_by(id=id_ordem)

        return SqlalchemyOrmPage(consulta,)