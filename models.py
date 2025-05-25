from pydantic import BaseModel
from typing import Optional

class PriceRequest(BaseModel):
    url: str
    title: str
    price: float
    currency: Optional[str] = None
    sku: Optional[str] = None
    brand: Optional[str] = None
    category: Optional[str] = None
    image: Optional[str] = None
    condition: Optional[str] = None
    availability: Optional[str] = None
    rating: Optional[float] = None
    reviewCount: Optional[int] = None
    seller: Optional[str] = None
    originalPrice: Optional[float] = None

class PriceResponse(BaseModel):
    url: str
    title: str
    price: str
    retailer_icon_url: str
