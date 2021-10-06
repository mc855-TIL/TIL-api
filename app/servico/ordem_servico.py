from typing import List

from app.api.response.ordem_response import (
    ListaOrdemResponse, OrdemResponse,
    VisualizaOrdemResponse
)
from app.repositorio import OrdemRepositorio


class OrdemServico:
    def __init__(self, ordem_repositorio: OrdemRepositorio) -> None:
        self.ordem_repositorio = ordem_repositorio

    def listar_ordens(
        self,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos

        Args:
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """
        ordens = self.ordem_repositorio.listar_ordens(
            pagina=pagina,
            limite=limite,
        )

        return ListaOrdemResponse.parse_obj(ordens.__dict__)

    def buscar_ordens(
        self,
        pesquisa: str,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos de acordo com a pesquisa

        Args:
            pesquisa (str): campo de pesquisa.
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """

        ordens = self.ordem_repositorio.buscar_ordens(
            pesquisa=pesquisa,
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

        Returns:
            OrdemResponse: Ordem buscada
        """

        ordem = self.ordem_repositorio.visualizar_ordem(
            id_ordem=id_ordem,
            auth=auth
        )
        print('Servico ordem = ', ordem)
        print(ordem.dataPublicacao.year)
        return ordem
