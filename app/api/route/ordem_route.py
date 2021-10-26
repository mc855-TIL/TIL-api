from typing import List, Optional

from app.api.response.ordem_response import ListaOrdemResponse, VisualizaOrdemResponse
from app.config.settings import settings
from app.container import get_ordem_servico
from app.servico import OrdemServico
from app.utils.enums import AcaoOrdemEnum, areaConhecimentoEnum, TipoOrdemEnum
from fastapi import APIRouter, Depends
from fastapi.param_functions import Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

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
    area_conhecimento: Optional[List[areaConhecimentoEnum]] = Query([]),
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

        - **area_conhecimento** (Optional[List[areaConhecimentoEnum]], optional):
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
        area_conhecimento=area_conhecimento,
        emprestimo=emprestimo,
        pagina=pagina,
        limite=limite,
    )


@app.get(
    "/ordens/{id_ordem}",
    response_model=VisualizaOrdemResponse,
    summary="Visualização de ordem através do ID",
)
def visualizar_ordem(
    id_ordem: int,
    auth: Optional[bool] = False,
    servico: OrdemServico = Depends(get_ordem_servico),
) -> VisualizaOrdemResponse:
    """
    Visualiza apenas uma ordem. Recupera os dados através da ID
    (Método para usuário anônimo do site)

    **Args**:

        **id_ordem** (int): ID da ordem requisitada
        **auth(Optional[bool])**: Flag que diz se o user está autenticado ou não
        True = autenticado; False = não autenticado

    **Returns**:

         - **VisualizaOrdemResponse**:  Modelo de resposta.
    """
    return servico.visualizar_ordem(id_ordem=id_ordem, auth=auth)
