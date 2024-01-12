import unittest
from api import call_api


class TestAPI(unittest.TestCase):
    def test_call_api(self):
        test_api_url = "https://api.frankfurter.app/currencies"
        test_expected_status_code = 200
        self.assertEqual(call_api(test_api_url).status_code, test_expected_status_code)

if __name__ == '__main__':
    unittest.main(exit=False)