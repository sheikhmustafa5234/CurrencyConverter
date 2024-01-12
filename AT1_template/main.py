import sys
from api import call_api, format_latest_url
from currency import CURRENCIES, check_valid_currency, extract_api_result
from checks import check_arguments,get_rate

def main():
    check_arguments()
    get_rate()



if __name__ == "__main__":
    main()
