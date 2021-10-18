from typing import List, Optional

from app.api.response.ordem_response import ListaOrdemResponse
from app.config.settings import settings
from app.container import get_ordem_servico
from app.servico import OrdemServico
from app.utils.enums import AcaoOrdemEnum, AreaConhecimentoEnum, TipoOrdemEnum
from fastapi import APIRouter, Depends
from fastapi.param_functions import Query

app = APIRouter()


@app.get(
    "/ordens",
    response_model=ListaOrdemResponse,
    summary="Lista de ordens de insumos.",
)
def listar_ordens(
    pesquisa: Optional[str] = None,
    acao: Optional[AcaoOrdemEnum] = None,
    nomeInst: Optional[str] = None,
    tipo: Optional[List[TipoOrdemEnum]] = Query([]),
    areaConhecimento: Optional[List[AreaConhecimentoEnum]] = Query([]),
    emprestimo: Optional[bool] = None,
    servico: OrdemServico = Depends(get_ordem_servico),
    pagina: Optional[int] = 1,
    limite: Optional[int] = settings.QUANTIDADE_PAGINA,
) -> ListaOrdemResponse:
    """Listagem de ordens.

    **Args**:

        - **pesquisa** (Optional[str]):
            Pesquisa de item.

        - **acao** (Optional[AcaoOrdemEnum]):
            Oferta/Pedido.

        - **nomeInst** (Optional[str]):
            Filtra pelo nome da instituição.

        - **tipo** (Optional[List[TipoOrdemEnum]], optional):
            Filtra pelo tipo de ordem (Insumo/Livro).

        - **areaConhecimento** (Optional[List[AreaConhecimentoEnum]], optional):
            Filtra pela área de conhecimento.

        - **emprestimo** (Optional[bool], optional):
            Filtra se a ordem é um emprestimo.

        - **pagina** (Optional[int], optional):
            Numero da página de dados.

        - **limite** (Optional[int], optional):
            Quantidade de ordens por página.

    **Returns**:

         - **ListaOrdemResponse**:  Modelo de resposta.
    """
    return servico.listar_ordens(
        pesquisa=pesquisa,
        acao=acao,
        nomeInst=nomeInst,
        tipo=tipo,
        areaConhecimento=areaConhecimento,
        emprestimo=emprestimo,
        pagina=pagina,
        limite=limite,
    )
