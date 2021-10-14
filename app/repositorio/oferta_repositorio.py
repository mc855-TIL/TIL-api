from sqlalchemy.orm.session import Session


class OfertaRepositorio:
    def __init__(self, sessao: Session) -> None:
        self.sessao = sessao
