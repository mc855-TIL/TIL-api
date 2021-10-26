from enum import Enum


class areaConhecimentoEnum(Enum):
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
    EM_NEGOCIACAO = "EM_NEGOCIACAO"
    FINALIZADO = "FINALIZADO"
