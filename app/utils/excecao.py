from typing import Optional


class ExcecaoBase(Exception):
    def __init__(self, msg: Optional[str] = ""):
        self.msg = msg


class ExcecaoNaoAutenticado(ExcecaoBase):
    pass


class ExcecaoRegraNegocio(ExcecaoBase):
    pass
