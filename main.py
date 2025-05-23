from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


allowed_origins = [
    "http://localhost:8000",
    "https://api.pricecomparison.fyi",
    "https://www.amazon.es",
    "https://www.mediamarkt.es",
    "https://www.pccomponentes.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/v1/prices")
def get_prices(url: str = Header(alias="X-Product-URL")):

    print(url)
    
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