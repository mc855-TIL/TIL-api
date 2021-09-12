from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.route.oferta_route import app as oferta_app

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

app.include_router(oferta_app, tags=["Ofertas"])
