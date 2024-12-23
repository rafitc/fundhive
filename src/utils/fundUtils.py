import requests
from config.config import RapidAPISettings
from model.fundModel import BuyFundPayload
from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend

def get_latest_price_from_scheme(fund_family, scheme_code):
    rapid = RapidAPISettings()
    url = "https://latest-mutual-fund-nav.p.rapidapi.com/latest"

    querystring = {"Mutual_Fund_Family":f"{fund_family}","Scheme_Type":"Open","Scheme_Category":f"{scheme_code}"}

    headers = {
        "x-rapidapi-key": f"{rapid.key}",
        "x-rapidapi-host": f"{rapid.host}"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response:
        return response
    
    return None