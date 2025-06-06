from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from models import PriceRequest
from prices import fetch_prices

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
    """Return a list of retailers selling the same product at an equal or lower price"""

    print(f"URL: {price.url}")
    print(f"Title: {price.title}")
    print(f"Price: {price.price}")
    print(f"Country Code: {price.country_code}")

    prices = fetch_prices(query=price.title, country_code=price.country_code, original_price=price.price)
    return {"prices": prices}


@app.get("/c")
def track_click(url: str = Query(...)):
    """Track click and redirect to the provided URL"""

    print(f"Click: {url}")
    return RedirectResponse(url=url, status_code=302)