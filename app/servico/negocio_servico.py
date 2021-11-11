from datetime import datetime, timedelta
from typing import List

from app.api.response.negocio_response import ListaNegocioResponse, NegocioResponse
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

    def listar_negocios(
        self,
        id_ordem: int,
        auth: bool,
    ) -> ListaNegocioResponse:
        """Listagem das ordens de insumos

        Args:
            id_ordem (int): ID da ordem requisitada
            auth(bool): Flag que diz se o user está autenticado ou não.
        Returns:
            ListaNegocioResponse: Listagem de ordens paginada
        """
        if auth:
            filtros = []
            filtros.append(Negocio.id_ordem == id_ordem)

            negocios = self.negocio_repositorio.listar_negocios(filtros)
            items = []
            for i, negocio in enumerate(negocios):
                items.append(NegocioResponse.parse_obj(negocio))
            ret = ListaNegocioResponse(items=items)
            return ret
        else:
            raise ExcecaoNaoAutenticado

    def deletar_todos_negocios_ordem(
        self,
        id_ordem: int,
        auth: bool,
    ):
        """Apaga todos os negócios de uma ordem através do ID da ordem.
        Args:
            id_ordem (int): ID da ordem requisitada
            auth(bool): Flag que diz se o user está autenticado ou não.

        Raises:"""
        if auth:
            self.negocio_repositorio.deletar_todos_negocios_ordem(id_ordem=id_ordem)
        else:
            raise ExcecaoNaoAutenticado


    def deletar_negocio(
        self,
        id_negocio: int,
        auth: bool,
    ):
        """Apaga um negócio de uma ordem através do ID do negócio.
        Args:
            id_ordem (int): ID da ordem requisitada
            auth(bool): Flag que diz se o user está autenticado ou não.

        Raises:"""
        if auth:
            self.negocio_repositorio.deletar_negocio(id_negocio=id_negocio)
        else:
            raise ExcecaoNaoAutenticado
