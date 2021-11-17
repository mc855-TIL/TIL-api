from datetime import date
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class NegocioResponse(BaseResponse):
    id: int
    nome_solicitante: str
    nome_instituicao: str


class ListaNegocioResponse(BaseResponse):
    items: List[NegocioResponse]
