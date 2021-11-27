from enum import Enum


class AreaConhecimentoEnum(Enum):
    BIOLOGICAS = "Biológicas"
    EXATAS = "Exatas"
    HUMANAS = "Humanas"
    TECNOLOGIAS = "Tecnologias"


class TipoOrdemEnum(Enum):
    INSUMO = "I"
    LIVRO = "L"


class AcaoOrdemEnum(Enum):
    OFERTA = "O"
    PEDIDO = "P"


class StatusOrdemEnum(Enum):
    DISPONIVEL = "DISPONIVEL"
    DESPUBLICADO = "DESPUBLICADO"
    FINALIZADO = "FINALIZADO"
    APAGADO = "APAGADO"


class StatusNegocioEnum(Enum):
    EM_NEGOCIACAO = "EM_NEGOCIACAO"
    ATENDIDO = "ATENDIDO"
    CANCELADO = "CANCELADO"


class ModoListaNegocios(Enum):
    ORDEM = "ORDEM"
    NEGOCIO = "NEGOCIO"
    MINHAS_SOLICITACOES = "MINHAS_SOLICITACOES"
