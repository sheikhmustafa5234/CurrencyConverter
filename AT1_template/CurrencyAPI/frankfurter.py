from api import call_api, format_currencies_url
from dataclasses import dataclass
_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'
from api import get_currencies

CURRENCIES = get_currencies()

class Frankfurter:
    _HOST_ = 'https://api.frankfurter.app'
    _CURRENCIES_ = '/currencies'
    _LATEST_ = '/latest'

    def get_currencies(self):
        data = call_api(format_currencies_url()).json()
        key_extract = list(data.keys())
        return key_extract


    def format_latest_url(from_currency: str, to_currency: str) -> str:
        latest_URL = _HOST_ + _LATEST_ + "?from=" + from_currency + "&to=" + to_currency

        return latest_URL

