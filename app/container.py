from fastapi import Depends
from sqlalchemy.orm.session import Session

from app.config.conexao import get_session
from app.repositorio import OrdemRepositorio, NegocioRepositorio
from app.servico import OrdemServico, NegocioServico


def get_ordem_repo(sessao: Session = Depends(get_session)):
    yield OrdemRepositorio(sessao=sessao)


def get_ordem_servico(
    ordem_repositorio: OrdemRepositorio = Depends(get_ordem_repo),
):
    yield OrdemServico(ordem_repositorio=ordem_repositorio)


def get_negocio_repo(sessao: Session = Depends(get_session)):
    yield NegocioRepositorio(sessao=sessao)


def get_negocio_servico(
    negocio_repositorio: OrdemRepositorio = Depends(get_negocio_repo),
):
    yield NegocioServico(negocio_repositorio=negocio_repositorio)
