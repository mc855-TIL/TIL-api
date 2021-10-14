from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.config.connection import get_session
from app.repositorio import *


def get_oferta_repo(sessao: Session = Depends(get_session)):
    yield OfertaRepositorio(sessao=sessao)


def get_oferta_servico(oferta_repositorio: OfertaRepositorio = Depends(get_oferta_repo)):
    from app.servico import OfertaServico

    yield OfertaServico(oferta_repositorio=oferta_repositorio)
