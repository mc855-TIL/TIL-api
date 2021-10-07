from typing import List

from app.api.response.ordem_response import (
    ListaOrdemResponse, OrdemResponse,
    VisualizaOrdemResponse
)
from app.repositorio import OrdemRepositorio
from pydantic import ValidationError

class OrdemServico:
    def __init__(self, ordem_repositorio: OrdemRepositorio) -> None:
        self.ordem_repositorio = ordem_repositorio

    def listar_ordens(
        self,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos

        Args:
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """
        ordens = self.ordem_repositorio.listar_ordens(
            pagina=pagina,
            limite=limite,
        )

        return ListaOrdemResponse.parse_obj(ordens.__dict__)

    def buscar_ordens(
        self,
        pesquisa: str,
        pagina: int,
        limite: int,
    ) -> ListaOrdemResponse:
        """Listagem das ordens de insumos de acordo com a pesquisa

        Args:
            pesquisa (str): campo de pesquisa.
            pagina (int): Pagina de dados.
            limite (int): Limite de dados por página.

        Returns:
            ListaOrdemResponse: Listagem de ordens paginada
        """

        ordens = self.ordem_repositorio.buscar_ordens(
            pesquisa=pesquisa,
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
        Visualiza apenas uma ordem. Recupera os dados através da ID
        (Método para usuário anônimo do site)
        Args:
        id_ordem (int): ID da ordem requisitada
        auth(bool): Flag que diz se o user está autenticado ou não
        True = autenticado; False = não autenticado
        Returns:
            VisualizaOrdemResponse: Detalhes da ordem buscada
        """
        if auth:
            ordem = self.ordem_repositorio.visualizar_ordem_autenticado(
                id_ordem=id_ordem,
            )
            if ordem:
                response = VisualizaOrdemResponse(
                    id = ordem[0],
                    acao = ordem[1],
                    item = ordem[2],
                    descricao = ordem[3],
                    nomeInst = ordem[4],
                    areaConhecimento = ordem[5],
                    emprestimo = ordem[6],
                    dataPublicacao = ordem[7],
                    dataValidade = ordem[8],
                    contato = ordem[9]
                )
        else:
            # try:
            ordem = self.ordem_repositorio.visualizar_ordem(
                id_ordem=id_ordem,
            )
            try:
                return VisualizaOrdemResponse(
                    id = ordem[0],
                    acao = ordem[1],
                    item = ordem[2],
                    descricao = ordem[3],
                    nomeInst = ordem[4],
                    areaConhecimento = ordem[5],
                    emprestimo = ordem[6],
                    dataPublicacao = ordem[7],
                    dataValidade = ordem[8],
                )
            except:
                print('Deu ruim!!!!!!!!!!!!!!!!!!!!!!!!!!!')

