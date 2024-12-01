from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    title: str
    description: str | None
    unit_price: float


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
