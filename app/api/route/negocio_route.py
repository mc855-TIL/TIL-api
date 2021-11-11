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


@app.delete(
    "/negocios/all/{id_ordem}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apagar todos os negócios de uma ordem através do ID da ordem",
)
def deletar_todos_negocios_ordem(
    id_ordem: int,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> None:
    """Apaga todos os negócios de uma ordem através do ID da ordem

    **Args**:
        **id_ordem** (int):
            ID da ordem

        **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
        - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    return servico.deletar_todos_negocios_ordem(id_ordem=id_ordem, auth=auth)



@app.delete(
    "/negocios/{id_negocio}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apagar um negócio de uma ordem através do ID do negócio",
)
def deletar_ordem(
    id_negocio: int,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> None:
    """Apaga um negócio de uma ordem através do ID do negócio

    **Args**:
        **id_ordem** (int):
            ID da ordem

        **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
        - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    return servico.deletar_negocio(id_negocio=id_negocio, auth=auth)