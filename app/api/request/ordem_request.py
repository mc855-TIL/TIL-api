from datetime import date
from typing import Optional

from app.api.request import BaseRequest
from app.modelo.sqlite.ordem_modelo import Ordem
from app.utils.enums import *


class CriarOrdemRequest(BaseRequest):
    item: str
    descricao: str
    acao: AcaoOrdemEnum
    tipo: TipoOrdemEnum
    data_validade: Optional[date]
    emprestimo: bool
    area_conhecimento: AreaConhecimentoEnum
    quantidade: Optional[str]
    id_usuario: int

    class Meta:
        model = Ordem

    @property
    def instancia(self):

        atributos = self.dict(exclude_unset=True)

        return Ordem(
            item=atributos.get("item"),
            descricao=atributos.get("descricao"),
            acao=atributos.get("acao").value,
            tipo=atributos.get("tipo").value,
            data_validade=atributos.get("data_validade"),
            emprestimo=atributos.get("emprestimo"),
            area_conhecimento=atributos.get("area_conhecimento").value,
            quantidade=atributos.get("quantidade"),
            id_usuario=atributos.get("id_usuario"),
        )
