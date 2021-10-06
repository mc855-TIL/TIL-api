from typing import Optional

from app.api.response.ordem_response import ListaOrdemResponse, OrdemResponse, VisualizaOrdemResponse
from app.config.settings import settings
from app.container import get_ordem_servico
from app.servico import OrdemServico
from fastapi import APIRouter, Depends

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
    "/ordens/{pesquisa}",
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
    return servico.buscar_ordens(pesquisa=pesquisa, pagina=pagina, limite=limite)

@app.get(
    '/ordens/',
    response_model=VisualizaOrdemResponse,
    summary="Visualização de ordem através do ID",
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
    """
    return servico.visualizar_ordem(id_ordem=id_ordem, auth=auth)

