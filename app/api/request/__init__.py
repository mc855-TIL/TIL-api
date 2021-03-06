from pydantic import BaseModel


class BaseRequest(BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

    @property
    def instancia(self):
        return self.Meta.model(**self.dict(exclude_unset=True))
