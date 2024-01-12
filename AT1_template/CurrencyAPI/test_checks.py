import unittest
from checks import check_arguments


class TestCheckArguments(unittest.TestCase):
    def TestCheckArguments(self):
        test_api_url = "https://api.frankfurter.app/currencies"
        test_expected_status_code = 200
        self.assertEqual(check_arguments(test_api_url).status_code, test_expected_status_code)


if __name__ == '__main__':
    unittest.main()