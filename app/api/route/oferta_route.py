from app.config.settings import settings
from app.dependencia import get_oferta_servico
from fastapi import APIRouter, Depends

app = APIRouter()


@app.get("/ofertas", summary="Lista de ofertas de insumos.")
def listar_ofertas(
    servico: Depends(get_oferta_servico),
    pagina: int = 1,
    limite: int = settings.QUANTIDADE_PAGINA,
) -> None:

    servico.listar_ofertas()
    return


@app.get("/ofertas/{pesquisa}")
def buscar_ofertas(
    pesquisa: str,
    servico: Depends(get_oferta_servico),
    pagina: int = 1,
    limite: int = settings.QUANTIDADE_PAGINA,
) -> None:

    servico.buscar_ofertas
