from datetime import date
from typing import Optional

from app.api.request import BaseRequest
from app.modelo.sqlite.negocio_modelo import Negocio
from app.utils.enums import *


class CriarNegocioRequest(BaseRequest):
    id_ordem: int
    id_solicitante: int

    class Meta:
        model = Negocio

    @property
    def instancia(self):

        atributos = self.dict(exclude_unset=True)

        return Negocio(**atributos)


class AtualizaNegocioRequest(BaseRequest):
    id: int
    status: StatusNegocioEnum

    @property
    def instancia(self):

        atributos = self.dict(exclude_unset=True)

        return Negocio(
            id=atributos.get("id"),
            status=atributos.get("status").value,
        )
