from pydantic import BaseModel

class PriceRequest(BaseModel):
    url: str
    title: str
    price: float

class PriceResponse(BaseModel):
    url: str
    title: str
    price: str
    thumbnail_url: str
    retailer_name: str
    retailer_logo_url: str
