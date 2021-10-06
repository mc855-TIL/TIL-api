from datetime import date
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class OrdemResponse(BaseResponse):
    id: int
    item: str
    acao: str
    nomeInst: str
    emprestimo: bool
    areaConhecimento: str


class ListaOrdemResponse(PaginacaoResponse):
    items: List[OrdemResponse] = Field(alias="itens")

class VisualizaOrdemResponse(BaseResponse):
    id: int
    item: str
    descricao: str
    acao: str
    nomeInst: str
    emprestimo: bool
    areaConhecimento: str
    dataPublicacao: date
    dataValidade: Optional[date]
    contato: Optional[str]
