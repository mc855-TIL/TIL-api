from typing import Optional

from app.api.response.ordem_response import ListaOrdemResponse
from app.config.settings import settings
from app.dependencia import get_ordem_servico
from fastapi import APIRouter, Depends

app = APIRouter()


@app.get(
    "/ordens",
    response_model=ListaOrdemResponse,
    summary="Lista de ordens de insumos.",
)
def listar_ordens(
    servico: Depends(get_ordem_servico),
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
    pesquisa: str,
    servico: Depends(get_ordem_servico),
    pagina: Optional[int] = 1,
    limite: Optional[int] = settings.QUANTIDADE_PAGINA,
):
    """Listagem das ordens de insumos registradas de acordo com a pesquisa.

    Args:
        pesquisa (str): Campo para pesquisa.
        pagina (int, optional): Pagina de dados.
        limite (int, optional): Limite de dados por página.
    """
    return servico.buscar_ordens(pesquisa=pesquisa, pagina=pagina, limite=limite)
