from typing import List

from app.api.response.ordem_response import ListaOrdemResponse
from app.repositorio import OrdemRepositorio


class OrdemServico:
    def __init__(self, ordem_repositorio: OrdemRepositorio) -> None:
        self.ordem_repositorio = ordem_repositorio

    def listar_ordens(
        self,
    ) -> ListaOrdemResponse:
        ordens = self.ordem_repositorio.listar_ordens()
        pass

    def buscar_ofertas(self, pesquisa: str) -> ListaOrdemResponse:
        pass
