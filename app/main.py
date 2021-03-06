from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.exc import NoResultFound
from starlette.middleware.cors import CORSMiddleware

from app.api.route.negocio_route import app as negocio_app
from app.api.route.ordem_route import app as ordem_app
from app.utils.excecao import ExcecaoNaoAutenticado, ExcecaoRegraNegocio

# from fastapi.exceptions import

app = FastAPI(
    title="Projeto MC855 - API Troca de insumos de laboratório.",
    description="API para realizar a troca de insumos de laboratório.",
    version="1.1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.exception_handler(NoResultFound)
def manipulador_no_result_found(request: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"mensagem": "Registro não encontrado"},
    )


@app.exception_handler(ExcecaoRegraNegocio)
def manipulador_regra_negocio(request: Request, exc: ExcecaoRegraNegocio):
    msg = getattr(exc, "msg", "")
    return JSONResponse(status_code=status.HTTP_409_CONFLICT, content={"msg": msg})


@app.exception_handler(ExcecaoNaoAutenticado)
def manipulador_nao_autenticado(request: Request, exc: ExcecaoNaoAutenticado):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"msg": "Autenticação necessária."},
    )


app.include_router(ordem_app, tags=["Ordens"])
app.include_router(negocio_app, tags=["Negócios"])
