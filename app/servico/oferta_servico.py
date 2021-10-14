from app.repositorio import OfertaRepositorio


class OfertaServico:
    def __init__(self, oferta_repositorio: OfertaRepositorio) -> None:
        self.oferta_repositorio = oferta_repositorio
