import requests

_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'



def call_api(url: str) -> requests.models.Response:

    response = requests.get(url)
    return response

def format_currencies_url() -> str:

    currencies_URL = _HOST_+ _CURRENCIES_

    return currencies_URL


def get_currencies():


    data = call_api(format_currencies_url()).json()
    key_extract = list(data.keys())

    return key_extract


def format_latest_url(from_currency: str, to_currency: str) -> str:

    latest_URL = _HOST_+_LATEST_+"&from="+from_currency+"&to="+to_currency
    
    return latest_URL

