from datetime import datetime, timedelta
from typing import List

from app.api.request.negocio_request import CriarNegocioRequest
from app.modelo.sqlite.negocio_modelo import Negocio
from app.repositorio import NegocioRepositorio
from app.utils.enums import *
from app.utils.enums import StatusOrdemEnum
from app.utils.excecao import ExcecaoNaoAutenticado, ExcecaoRegraNegocio


class NegocioServico:
    def __init__(self, negocio_repositorio: NegocioRepositorio) -> None:
        self.negocio_repositorio = negocio_repositorio

    def criar_negocio(
        self,
        criar_negocio: CriarNegocioRequest,
        auth: bool,
    ):
        """Criar um negocio.

        Args:
            criar_negocio (CriarNegocioRequest): Dados da negocio.
            auth (bool): Flag de autenticação.

        Raises:
            ExcecaoRegraNegocio: Data validade não permitida
            ExcecaoNaoAutenticado: Usuario não autenticado.
        """

        if auth:
            # TODO: talvez criar um campo timestamp na tabela negocios
            # dia_atual = (datetime.utcnow() - timedelta(hours=3)).date()

            negocio = criar_negocio.instancia

            self.negocio_repositorio.criar_negocio(negocio=negocio)

        else:
            raise ExcecaoNaoAutenticado

