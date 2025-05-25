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
    print(f"URL: {price.url}")
    print(f"Title: {price.title}")
    print(f"Price: {price.price}")
    print(f"Currency: {price.currency}")
    print(f"SKU: {price.sku}")
    print(f"Brand: {price.brand}")
    print(f"Description: {price.description}")
    print(f"Category: {price.category}")
    print(f"Image: {price.image}")
    print(f"Condition: {price.condition}")
    print(f"Availability: {price.availability}")
    print(f"Rating: {price.rating}")
    print(f"Review Count: {price.reviewCount}")
    print(f"Seller: {price.seller}")
    print(f"Original Price: {price.originalPrice}")
    
    prices = [
        {
            "url": "https://www.mediamarkt.es/es/product/_apple-iphone-16-rosa-128-gb-5g-61-oled-super-retina-xdr-chip-a18-bionic-ios-1582152.html",
            "title": "Apple iPhone 16, Rosa, 128 GB, 5G, 6.1 OLED Super Retina XDR, Chip A18 Bionic, iOS",
            "price": "799.00€",
            "retailer_icon_url": "https://www.mediamarkt.es/public/manifest/favicon-Media-48x48.png"
        },
        {
            "url": "https://www.pccomponentes.com/movil-apple-iphone-16-128gb-rosa",
            "title": "Apple iPhone 16 128GB Rosa",
            "price": "819.00€",
            "retailer_icon_url": "https://cdn.pccomponentes.com/img/favicons/favicon.png"
        },
        {
            "url": "https://www.tradeinn.com/techinn/es/apple-iphone-16-128gb-6.1/141410946/p",
            "title": "Apple IPhone 16 128GB 6.1",
            "price": "878.99€",
            "retailer_icon_url": "https://www.tradeinn.com/web/favicon_0.ico"
        }
    ]

    return {"prices": prices}