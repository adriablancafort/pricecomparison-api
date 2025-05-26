from models import PriceRequest
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


es = Elasticsearch("http://localhost:9200")
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_prices(price: PriceRequest):
    query_text = f"{price.brand} {price.title} {price.category or ''}"
    query_embedding = model.encode(query_text).tolist()

    res = es.search(index="products", body={
        "knn": {
            "field": "embedding",
            "query_vector": query_embedding,
            "k": 10,
            "num_candidates": 100
        },
        "query": {
            "bool": {
                "filter": [
                    {"range": {"price": {"lt": price.price}}}
                ]
            }
        },
        "_source": ["url", "title", "price", "seller", "image"]
    })

    prices = []
    for hit in res["hits"]["hits"]:
        product = hit["_source"]
        prices.append({
            "url": product["url"],
            "title": product["title"],
            "price": f"{product['price']}€",
            "retailer_icon_url": get_favicon(product["url"])
        })

    return {"prices": prices}