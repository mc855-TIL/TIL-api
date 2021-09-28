from datetime import date
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class OrdemResponse(BaseResponse):
    item: str
    descricao: str
    data_publicacao: date
    data_validade: Optional[date]
    tipo_acao: str
    tipo_item: str
    nome_instituto: str
    emprestimo: bool


class ListaOrdemResponse(PaginacaoResponse):
    items: List[OrdemResponse] = Field(alias="itens")
