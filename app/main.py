from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm.exc import NoResultFound
from starlette.middleware.cors import CORSMiddleware

from app.api.route.ordem_route import app as ordem_app

app = FastAPI(
    title="Projeto MC855 - API Troca de insumos de laboratório.",
    description="API para realizar a troca de insumos de laboratório.",
    version="1.0",
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
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"mensagem": "Registro não encontrado"})


app.include_router(ordem_app, tags=["Ordens"])
