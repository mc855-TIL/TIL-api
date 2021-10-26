from typing import List

from app.api.response.ordem_response import ListaOrdemResponse, VisualizaOrdemResponse
from app.modelo.sqlite.ordem_modelo import Ordem
from app.repositorio import OrdemRepositorio
from app.utils.enums import *


class OrdemServico:
    def __init__(self, ordem_repositorio: OrdemRepositorio) -> None:
        self.ordem_repositorio = ordem_repositorio

    def listar_ordens(
        self,
        pesquisa: str,
        acao: AcaoOrdemEnum,
        nomeInst: str,
        tipo: List[TipoOrdemEnum],
        area_conhecimento: List[area_conhecimentoEnum],
        emprestimo: bool,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos

        Args:
            pesquisa (str): campo de pesquisa.
            acao (AcaoOrdemEnum): Oferta/Pedido.
            nomeInst (str): Nome da Instituição.
            tipo (List[TipoOrdemEnum]): Lista com os tipos de insumos.
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """

        filtros = []
        if pesquisa:
            filtros.append(Ordem.item.ilike(f"%{pesquisa}%"))

        if acao:
            filtros.append(Ordem.acao == acao.value)

        if nomeInst:
            filtros.append(Ordem.nomeInst == nomeInst)

        if tipo:
            lista_tipo = [item.value for item in tipo]
            filtros.append(Ordem.tipo.in_(lista_tipo))

        if area_conhecimento:
            lista_area = [area.value for area in area_conhecimento]
            filtros.append(Ordem.area_conhecimento.in_(lista_area))

        if isinstance(emprestimo, bool):
            filtros.append(Ordem.emprestimo.is_(emprestimo))

        ordens = self.ordem_repositorio.listar_ordens(
            filtros=filtros,
            pagina=pagina,
            limite=limite,
        )

        return ListaOrdemResponse.parse_obj(ordens.__dict__)

    def visualizar_ordem(
        self,
        id_ordem: int,
        auth: bool,
    ) -> VisualizaOrdemResponse:
        """
        Visualiza apenas uma ordem. Recupera os dados através da ID
        (Método para usuário anônimo do site)
        Args:
        id_ordem (int): ID da ordem requisitada
        auth(bool): Flag que diz se o user está autenticado ou não
        True = autenticado; False = não autenticado
        Returns:
            VisualizaOrdemResponse: Detalhes da ordem buscada
        """
        if auth:
            ordem = self.ordem_repositorio.visualizar_ordem_autenticado(
                id_ordem=id_ordem,
            )
        else:
            ordem = self.ordem_repositorio.visualizar_ordem(
                id_ordem=id_ordem,
            )

        return VisualizaOrdemResponse.from_orm(ordem)
