from typing import List, Optional

from app.api.response.negocio_response import ListaNegocioResponse
from app.api.request.negocio_request import CriarNegocioRequest
from app.config.settings import settings
from app.container import get_negocio_servico
from app.servico import NegocioServico
from fastapi import APIRouter, Depends, status
from fastapi.param_functions import Query

app = APIRouter()


@app.get(
    "/negocios/{id_ordem}",
    response_model=ListaNegocioResponse,
    summary="Lista de negocios de uma ordem.",
)
def listar_negocios(
    id_ordem: int,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> ListaNegocioResponse:
    """Listagem de ordens.

    **Args**:

       **id_ordem** (int):
            ID da ordem requisitada

       **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.
    **Raises**:
        - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    return servico.listar_negocios(
        id_ordem, auth,
    )


@app.post(
    "/negocios",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Cria uma negociação nova a partir de um interesse do usuario.",
)
def criar_negocio(
    criar_negocio: CriarNegocioRequest,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> None:
    """Criar uma nova negociação de um item em anúncio.

    **Args**:
        - **criar_negocio** (CriarNegocioRequest):
            Corpo da requisiçãao.

        - **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
        - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """

    servico.criar_negocio(criar_negocio=criar_negocio, auth=auth)
