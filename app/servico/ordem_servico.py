from datetime import datetime, timedelta
from typing import List

from app.api.request.ordem_request import CriarOrdemRequest
from app.api.response.ordem_response import ListaOrdemResponse, VisualizaOrdemResponse, ListaItemResponse
from app.modelo.sqlite.ordem_modelo import Ordem
from app.repositorio import OrdemRepositorio
from app.utils.enums import *
from app.utils.enums import StatusOrdemEnum
from app.utils.excecao import ExcecaoNaoAutenticado, ExcecaoRegraNegocio


class OrdemServico:
    def __init__(self, ordem_repositorio: OrdemRepositorio) -> None:
        self.ordem_repositorio = ordem_repositorio

    def listar_ordens(
        self,
        pesquisa: str,
        acao: AcaoOrdemEnum,
        nomeInst: str,
        tipo: List[TipoOrdemEnum],
        area_conhecimento: List[AreaConhecimentoEnum],
        emprestimo: bool,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos

        Args:
            pesquisa (str): campo de pesquisa.
            acao (AcaoOrdemEnum): Oferta/Pedido.
            nomeInst (str): Nome da Instituição.
            tipo (List[TipoOrdemEnum]): Lista com os tipos de insumos.
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """

        filtros = []
        if pesquisa:
            filtros.append(Ordem.item.ilike(f"%{pesquisa}%"))

        if acao:
            filtros.append(Ordem.acao == acao.value)

        if nomeInst:
            filtros.append(Ordem.nomeInst == nomeInst)

        if tipo:
            lista_tipo = [item.value for item in tipo]
            filtros.append(Ordem.tipo.in_(lista_tipo))

        if area_conhecimento:
            lista_area = [area.value for area in area_conhecimento]
            filtros.append(Ordem.area_conhecimento.in_(lista_area))

        if isinstance(emprestimo, bool):
            filtros.append(Ordem.emprestimo.is_(emprestimo))

        ordens = self.ordem_repositorio.listar_ordens(
            filtros=filtros,
            pagina=pagina,
            limite=limite,
        )

        return ListaOrdemResponse.parse_obj(ordens.__dict__)

    def visualizar_ordem(
        self,
        id_ordem: int,
        auth: bool,
    ) -> VisualizaOrdemResponse:
        """
        Visualiza apenas uma ordem.

        Args:
            id_ordem (int): ID da ordem requisitada
            auth(bool): Flag que diz se o user está autenticado ou não.

        Returns:
            VisualizaOrdemResponse: Detalhes da ordem buscada
        """
        if auth:
            ordem = self.ordem_repositorio.visualizar_ordem_autenticado(
                id_ordem=id_ordem,
            )
        else:
            ordem = self.ordem_repositorio.visualizar_ordem(
                id_ordem=id_ordem,
            )

        return VisualizaOrdemResponse.from_orm(ordem)

    def criar_ordem(
        self,
        criar_ordem: CriarOrdemRequest,
        auth: bool,
    ):
        """Criar uma ordem.

        Args:
            criar_ordem (CriarOrdemRequest): Dados da ordem.
            auth (bool): Flag de autenticação.

        Raises:
            ExcecaoRegraNegocio: Data validade não permitida
            ExcecaoNaoAutenticado: Usuario não autenticado.
        """

        if auth:
            dia_atual = (datetime.utcnow() - timedelta(hours=3)).date()

            ordem = criar_ordem.instancia

            if ordem.data_validade < dia_atual:
                raise ExcecaoRegraNegocio(msg="Data validade menor que a data atual.")

            ordem.data_publicacao = dia_atual
            ordem.status = StatusOrdemEnum.DISPONIVEL.value
            self.ordem_repositorio.criar_ordem(ordem=ordem)

        else:
            raise ExcecaoNaoAutenticado

    def pesquisar_nome_item(
        self,
        nome_item: str,
        auth: bool,
    ) -> ListaItemResponse:
        """Criar uma ordem.

        Args:
            nome_item (str):Nome do item.
            auth (bool): Flag de autenticação.

        Raises:
            ExcecaoNaoAutenticado: Usuario não autenticado.
        """
        if auth:
            filtros = []
            filtros.append(Ordem.item.ilike(f"%{nome_item}%"))

            resp = self.ordem_repositorio.pesquisar_nome_item(
                nome_item=nome_item,
                filtros=filtros,
            )
            str_list =  []
            for i, item in enumerate(resp):
                str_list.append(item[0])

            listItemResp = ListaItemResponse(items=str_list)
            # listItemResp.items = str_list

            return listItemResp
        else:
            raise ExcecaoNaoAutenticado
