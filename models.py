from pydantic import BaseModel

class PriceRequest(BaseModel):
    url: str
    title: str
    price: float
