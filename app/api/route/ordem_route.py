from app.api.response.ordem_response import ListaOrdemResponse
from app.config.settings import settings
from app.dependencia import get_oferta_servico
from fastapi import APIRouter, Depends

app = APIRouter()


@app.get("/ordens", response_model=ListaOrdemResponse, summary="Lista de ordens de insumos.")
def listar_ordens(
    servico: Depends(get_oferta_servico),
    pagina: int = 1,
    limite: int = settings.QUANTIDADE_PAGINA,
) -> None:

    servico.listar_ofertas()
    return


@app.get("/ordens/{pesquisa}", response_model=ListaOrdemResponse, summary="Lista de ordens de insumos com base em uma pesquisa.")
def buscar_ordens(
    pesquisa: str,
    servico: Depends(get_oferta_servico),
    pagina: int = 1,
    limite: int = settings.QUANTIDADE_PAGINA,
) -> None:

    servico.buscar_ofertas
