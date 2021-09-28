from typing import List

import paginate
from app.api.response.ordem_response import ListaOrdemResponse
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

    def buscar_ofertas(
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
