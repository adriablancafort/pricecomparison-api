from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/prices")
def get_prices():
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

    return prices