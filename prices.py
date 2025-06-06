import requests
import json
from urllib.parse import urlparse


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


def process_prices(kelkoo_data, original_price, original_url):
    """Process Kelkoo API data into formatted price list"""
    
    original_domain = urlparse(original_url).netloc.lower()

    prices = []
    for offer in kelkoo_data.get('offers', []):
        offer_price = offer.get('price', 0)

        lower_price_limit = 0.7 * original_price

        # Skip prices higher than original price
        if offer_price > original_price or offer_price < lower_price_limit:
            continue
        
        offer_url = offer.get('offerUrl', {}).get('landingUrl', '').split('?')[0]
        offer_domain = urlparse(offer_url).netloc.lower()

        # Skip if same retailer as original
        if offer_domain == original_domain:
            continue
        
        # Calculate savings
        savings = round(original_price - offer_price)
        
        # Generate favicon URL from the retailer domain
        favicon_url = f"https://www.google.com/s2/favicons?domain={offer_domain}&sz=48"

        price_data = {
            "url": offer_url,
            "title": offer.get('title', ''),
            "price": f"{offer_price:.2f}€",
            "savings": f"{savings}€",
            "retailer_icon_url": favicon_url,
            "price_value": offer_price  # For sorting
        }
        prices.append(price_data)
    
    # Sort by price (cheapest first) and remove the sorting helper
    prices.sort(key=lambda x: x['price_value'])
    for price in prices:
        del price['price_value']
    
    return prices


def fetch_prices(query='iPhone 16', country_code='es', page_size=8, original_price=1000, original_url=""):
    """Fetch and process prices from Kelkoo API"""

    kelkoo_data = fetch_kelkoo_api(query, country_code, page_size)
    return process_prices(kelkoo_data, original_price, original_url)


if __name__ == "__main__":
    prices = fetch_prices("iphone 16")
    print(json.dumps(prices))