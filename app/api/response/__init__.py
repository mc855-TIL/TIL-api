from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class PaginacaoResponse(BaseResponse):
    item_count: int = Field(None, alias="total")
    page_count: int = Field(None, alias="total_paginas")
    previous_page: str = Field(None, alias="pagina_anterior")
    next_page: str = Field(None, alias="proxima_pagina")
    first_page: int = Field(None, alias="primeira_pagina")
    last_page: int = Field(None, alias="ultima_pagina")
