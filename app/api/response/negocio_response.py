from datetime import date, datetime
from typing import List, Optional

from pydantic.fields import Field

from . import BaseResponse, PaginacaoResponse


class NegocioResponse(BaseResponse):
    id: int
    status: str
    nome_ordem: Optional[str]
    nome_solicitante: Optional[str]
    nome_instituicao: Optional[str]
    email_solicitante: Optional[str]
    contato_solicitante: Optional[str]
    nome_instituicao: Optional[str]
    data_hora_criacao: Optional[datetime]
    data_hora_resposta: Optional[datetime]


class ListaNegocioResponse(BaseResponse):
    items: List[NegocioResponse]
