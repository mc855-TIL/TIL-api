import sqlalchemy as sa

from .ordem_modelo import Ordem  # noqa

sa.orm.configure_mappers()
