import sys
import datetime
from api import call_api, format_latest_url
from currency import CURRENCIES, check_valid_currency, extract_api_result



def main():

    if len(sys.argv) < 3:
        print("[ERROR] You need to provide 3 arguments in the following order: date <currency1> <currency2>")
    else:
        if len(sys.argv) == 3:
            if sys.argv[1] != sys.argv[2]:
                final_result = get_rate(sys.argv[1], sys.argv[2])
                return print(final_result)
            else:
                print("There is an error with API call")
        else:
            print("There is an error with API call")
     

def get_rate(from_currency: str, to_currency: str):

    from_currency_result = check_valid_currency(from_currency)
    to_currency_result = check_valid_currency(to_currency)
    url = format_latest_url(from_currency, to_currency)
        
    if from_currency_result == True and to_currency_result == True:
        result = call_api(url).json()
        currency = extract_api_result(result)
        return currency.format_result()    
    else:
        if from_currency_result == True and to_currency_result == False:
            print(to_currency + " is not a valid option")
        elif from_currency_result == False and to_currency_result == True:
            print(from_currency + " is not a valid option")
        elif from_currency_result == False and to_currency_result == False:
            print(from_currency + " and " + to_currency + " is not a valid option")
    exit()

if __name__ == "__main__":
    main()
