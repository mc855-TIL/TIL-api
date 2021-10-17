from typing import Optional

from app.api.response.ordem_response import ListaOrdemResponse, OrdemResponse, VisualizaOrdemResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.config.settings import settings
from app.container import get_ordem_servico
from app.servico import OrdemServico
from fastapi import APIRouter, Depends, HTTPException

app = APIRouter()


@app.get(
    "/ordens",
    response_model=ListaOrdemResponse,
    summary="Lista de ordens de insumos.",
)
def listar_ordens(
    servico: OrdemServico = Depends(get_ordem_servico),
    pagina: Optional[int] = 1,
    limite: Optional[int] = settings.QUANTIDADE_PAGINA,
):
    """Listagem das ordens de insumos registradas

    Args:
        pagina (int, optional): Pagina de dados.
        limite (int, optional): Limite de dados por página.
    """
    return servico.listar_ordens(pagina=pagina, limite=limite)


@app.get(
    '/ordens/{id_ordem}',
    response_model=VisualizaOrdemResponse,
    summary="Visualização de ordem através do ID",
    responses={404: {"model": BaseModel}}
    )
def visualizar_ordem(
    id_ordem: int,
    auth: Optional[bool] = False,
    servico: OrdemServico = Depends(get_ordem_servico),
):
    """
    Visualiza apenas uma ordem. Recupera os dados através da ID
    (Método para usuário anônimo do site)
    Args:
        id_ordem (int): ID da ordem requisitada
        auth(bool): Flag que diz se o user está autenticado ou não
        True = autenticado; False = não autenticado
    """
    ret = servico.visualizar_ordem(id_ordem=id_ordem, auth=auth)

    if ret is None:
        return  JSONResponse(status_code=404, content={"message": "Item não encontrado"})
        # raise HTTPException(status_code=404, detail="Item não encontrado")
    return ret



@app.get(
    "/ordens/",
    response_model=ListaOrdemResponse,
    summary="Lista de ordens de insumos com base em uma pesquisa.",
)
def buscar_ordens(
    pesquisa: Optional[str],
    servico: OrdemServico = Depends(get_ordem_servico),
    pagina: Optional[int] = 1,
    limite: Optional[int] = settings.QUANTIDADE_PAGINA,
):
    """Listagem das ordens de insumos registradas de acordo com a pesquisa.

    Args:
        pesquisa (str, optional): Campo para pesquisa.
        pagina (int, optional): Pagina de dados.
        limite (int, optional): Limite de dados por página.
    """
    try:
        response = servico.buscar_ordens(pesquisa=pesquisa, pagina=pagina, limite=limite)
    except:
        return {}

