import requests
import json
import os
from urllib.parse import quote, urlparse
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv('API_BASE_URL')


def fetch_kelkoo_api(query, country_code, page_size=10):
    """Fetch prices from Kelkoo API"""
    
    url = "https://www.kelkoo.es/api/shoppingapi"
    
    params = {
        'country': country_code.lower(),
        'fieldsAlias': 'all',
        'query': query,
        'pageSize': str(page_size),
        'page': '1',
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices: {e}")
        return None


def process_prices(kelkoo_data, original_price=None):
    """Process Kelkoo API data into formatted price list"""
    
    prices = []
    for offer in kelkoo_data.get('offers', []):
        offer_price = offer.get('price', 0)
        
        # Skip prices higher than original price
        if offer_price > original_price:
            continue
        
        # Calculate savings
        savings = round(original_price - offer_price)
        
        # Get original URL and create tracking URL
        original_url = offer.get('offerUrl', {}).get('landingUrl', '').split('?')[0]
        tracking_url = f"{API_BASE_URL}/c?url={quote(original_url)}"
        
        # Generate favicon URL from the retailer domain
        domain = urlparse(original_url).netloc
        favicon_url = f"https://www.google.com/s2/favicons?domain={domain}&sz=48"

        price_data = {
            "url": tracking_url,
            "title": offer.get('title', ''),
            "price": f"{offer_price:.2f}€",
            "savings": f"{savings}€" if savings > 0 else "0€",
            "retailer_icon_url": favicon_url,
            "price_value": offer_price  # For sorting
        }
        prices.append(price_data)
    
    # Sort by price (cheapest first) and remove the sorting helper
    prices.sort(key=lambda x: x['price_value'])
    for price in prices:
        del price['price_value']
    
    return prices


def fetch_prices(query='iPhone 16', country_code='es', page_size=8, original_price=1000):
    """Fetch and process prices from Kelkoo API"""

    kelkoo_data = fetch_kelkoo_api(query, country_code, page_size)
    return process_prices(kelkoo_data, original_price)


if __name__ == "__main__":
    prices = fetch_prices("iphone 16")
    print(json.dumps(prices))