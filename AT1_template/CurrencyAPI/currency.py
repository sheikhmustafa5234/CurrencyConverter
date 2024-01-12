from dataclasses import dataclass
from unittest import result

from api import get_currencies

CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:


    if currency in CURRENCIES:
        return True
    else:
        return False

@dataclass
class Currency:

    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):

        self.inverse_rate = round(1/self.rate, 5)

    def format_result(self):

        return "The conversion rate on " + self.date + " from " + self.from_currency + " to "+self.to_currency + " is " + str(self.rate) + ". The inverse rate is " + str(self.inverse_rate)


def extract_api_result(result: dict)->Currency:

        from_currency = result.get("base")
        to_currency = list(result.get("rates").keys())[0]
        amount = result.get("amount")
        rate = result.get("rates").get(to_currency)
        date = result.get("date")

        currency = Currency(from_currency, to_currency, amount, rate, None, date)
        currency.reverse_rate()

        return currency
