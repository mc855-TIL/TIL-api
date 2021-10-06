from typing import Optional

from app.api.response.ordem_response import ListaOrdemResponse
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
    pesquisa: Optional[str],
    nomeInst: Optional[Enum],
    servico: OrdemServico = Depends(get_ordem_servico),
    pagina: Optional[int] = 1,
    limite: Optional[int] = settings.QUANTIDADE_PAGINA,
):
    """Listagem das ordens de insumos registradas

    Args:
        pesquisa (str, optional): Campo para pesquisa.
        pagina (int, optional): Pagina de dados.
        limite (int, optional): Limite de dados por página.
    """
    return servico.listar_ordens(pagina=pagina, limite=limite)
