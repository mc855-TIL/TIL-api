from datetime import date
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class OrdemResponse(BaseResponse):
    id: int
    item: str
    acao: str
    nome_instituicao: str
    emprestimo: bool
    area_conhecimento: str


class ListaOrdemResponse(PaginacaoResponse):
    items: List[OrdemResponse] = Field(alias="itens")


class ListaItemResponse(BaseResponse):
    items: List[str]


class VisualizaOrdemResponse(BaseResponse):
    id: int
    item: str
    descricao: str
    acao: str
    tipo: str
    nome_instituicao: str
    emprestimo: bool
    area_conhecimento: str
    data_publicacao: date
    data_validade: Optional[date]
    usuario_id: Optional[int]
    nome: Optional[str]
    email: Optional[str]
    contato: Optional[str]
    quantidade: Optional[str]
