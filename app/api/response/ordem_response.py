from datetime import date
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class OrdemResponse(BaseResponse):
    id: int
    item: str
    tipo: str
    nomeInst: str
    emprestimo: bool
    areaConhecimento: str


class ListaOrdemResponse(PaginacaoResponse):
    items: List[OrdemResponse] = Field(alias="itens")
