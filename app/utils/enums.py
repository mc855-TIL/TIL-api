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
