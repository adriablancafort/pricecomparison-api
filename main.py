from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import PriceRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/v1/prices")
def get_prices(price: PriceRequest):
    print(f"Searching prices for: {price.title}")
    print(f"Original URL: {price.url}")
    print(f"Original price: ${price.price}")
    
    prices = [
        {
            "price": "$19.99",
            "link": "https://www.amazon.com/example-product",
            "store": "Amazon"
        },
        {
            "price": "$24.99",
            "link": "https://www.mediamarkt.es/es/product/_example-product-1234567.html",
            "store": "MediaMarkt"
        },
        {
            "price": "$17.99",
            "link": "https://www.pccomponentes.com/example-product",
            "store": "PCComponentes"
        }
    ]

    return {"prices": prices}