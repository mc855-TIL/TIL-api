from typing import List

from app.modelo.postgres.oferta_model import Oferta
from app.repositorio import OfertaRepositorio, oferta_repositorio


class OfertaServico:
    def __init__(self, oferta_repositorio: OfertaRepositorio) -> None:
        self.oferta_repositorio = oferta_repositorio

    def listar_ofertas(
        self,
    ) -> List[Oferta]:
        return self.oferta_repositorio.listar_ofertas()

    def buscar_ofertas(self, pesquisa: str) -> List[Oferta]:
        pass
