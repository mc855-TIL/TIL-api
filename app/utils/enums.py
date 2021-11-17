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


class StatusNegocioEnum(Enum):
    EM_NEGOCIACAO = "EM_NEGOCIACAO"
    ATENDIDO = "ATENDIDO"

class ModoListaNegocios(Enum):
    ORDEM = "ORDEM"
    NEGOCIO = "NEGOCIO"
    USUARIO = "USUARIO"