from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.config.connection import get_session
from app.repositorio import OrdemRepositorio


def get_ordem_repo(sessao: Session = Depends(get_session)):
    yield OrdemRepositorio(sessao=sessao)


def get_ordem_servico(ordem_repositorio: OrdemRepositorio = Depends(get_ordem_repo)):
    from app.servico import OrdemServico

    yield OrdemServico(ordem_repositorio=ordem_repositorio)
