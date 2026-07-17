from pydantic import BaseModel, Field, ConfigDict


class PoiCreate(BaseModel):
    name: str
    x: int = Field(ge=0)
    y: int = Field(ge=0)


class PoiRead(PoiCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
