import unittest
from api import call_api, format_currencies_url,format_latest_url
from frankfurter import Frankfurter

class TestCheckCurrency(unittest.TestCase):
        def test_format_currencies_url(self):
            test_format_currencies_url = "https://api.frankfurter.app/currencies"
            self.assertEqual(format_currencies_url(), test_format_currencies_url)


class TestHistoricalRate(unittest.TestCase):
    def test_format_latest_url(self):
        test_latest_url = "https://api.frankfurter.app/latest?from=GBP&to=AUD"
        test_from_currency = "GBP"
        test_to_currency = "AUD"
        self.assertEqual(format_latest_url(test_from_currency, test_to_currency), test_latest_url)


if __name__ == '__main__':
    unittest.main()