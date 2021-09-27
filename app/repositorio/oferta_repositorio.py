from typing import List

from app.modelo.postgres.oferta_model import Oferta
from sqlalchemy.orm.session import Session


class OfertaRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao

    def listar_ofertas(
        self,
    ) -> List[Oferta]:
        pass

    def buscar_ofertas(
        self,
    ) -> List[Oferta]:
        consulta = self.sessao.query(Oferta).all()

        return consulta
