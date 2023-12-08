from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    sku: Optional[str] = None
    name: str = Field(default="Name")
    price: float = Field(default=0, ge=0)
    brand: str
    consulted: int = Field(default=0)
