from app.config.settings import settings
from fastapi import APIRouter

app = APIRouter()


@app.get("/ofertas", summary="Lista de ofertas de insumos.")
def listar_ofertas(pagina: int = 1, limite: int = settings.QUANTIDADE_PAGINA) -> None:
    return {}
