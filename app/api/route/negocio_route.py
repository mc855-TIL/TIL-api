from typing import List, Optional

from app.api.response.negocio_response import ListaNegocioResponse
from app.api.request.negocio_request import CriarNegocioRequest, AtualizaNegocioRequest
from app.config.settings import settings
from app.container import get_negocio_servico
from app.servico import NegocioServico
from fastapi import APIRouter, Depends, status
from fastapi.param_functions import Query
from app.utils.enums import ModoListaNegocios

app = APIRouter()


@app.get(
    "/negocios/{id}",
    response_model=ListaNegocioResponse,
    summary="Lista de negocios de uma ordem.",
)
def listar_negocios(
    id: int,
    modo: ModoListaNegocios,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> ListaNegocioResponse:
    """Listagem de negocios.

    **Args**:
       - **id_ordem** (int):
            ID da ordem requisitada
        - **modo** (ModoListaNegocios)
            Modo de listar os negocios
       - **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
       - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    return servico.listar_negocios(
        id,
        modo,
        auth,
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
    "/negocios/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Apagar um ou todos os negócios de uma ordem",
)
def deletar_negocio(
    id: int,
    all: Optional[bool] = False,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> None:
    """Apaga um negócio de uma ordem através do ID
    do negócio ou todos através do ID da ordem

    **Args**:
       - **id** (int):
            ID da ordem ou negócio
        - **all** (Optional[bool])**:
            Flag que diz se são todas os negócios de uma ordem
        - **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
       - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    return servico.deletar_negocio(id=id, all=all, auth=auth)


@app.patch(
    "/negocios",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Atualiza um negócio de uma ordem de item.",
)
def atualiza_negocio(
    atualizar_negocio: AtualizaNegocioRequest,
    auth: Optional[bool] = False,
    servico: NegocioServico = Depends(get_negocio_servico),
) -> None:
    """Atualiza um negócio de uma nova ordem.

    **Args**:
       - **atualizar_negocio** (AtualizaNegocioRequest):
            Corpo da requisiçãao.
       - **auth(Optional[bool])**:
            Flag que diz se o user está autenticado ou não.

    **Raises**:
       - **ExcecaoNaoAutenticado**:
            Usuario não autenticado.
    """
    servico.atualiza_negocio(atualizar_negocio=atualizar_negocio, auth=auth)
