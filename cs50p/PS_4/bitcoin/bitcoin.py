import sys
import json
import requests

def main():
    bitcoins = float(input_data())
    rate = float(exchange_rate())
    conversion = bitcoins*rate
    print(f"${conversion:,.4f}")

def input_data():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    elif len(sys.argv) < 2:
        sys.exit("Command-line argument is too longer")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
    else:
        return sys.argv[1]

def exchange_rate():
    data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = data.json()
    return o.get("bpi").get("USD").get("rate_float")

main()


# {
#     "time": {
#         "updated": "Jan 25, 2023 16:56:00 UTC",
#         "updatedISO": "2023-01-25T16:56:00+00:00",
#         "updateduk": "Jan 25, 2023 at 16:56 GMT"
#     },
#     "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#     "chartName": "Bitcoin",
#     "bpi": {
#         "USD": {
#             "code": "USD",
#             "symbol": "&#36;",
#             "rate": "22,653.5171",
#             "description": "United States Dollar",
#             "rate_float": 22653.5171
#         },
#         "GBP": {
#             "code": "GBP",
#             "symbol": "&pound;",
#             "rate": "18,929.0977",
#             "description": "British Pound Sterling",
#             "rate_float": 18929.0977
#         },
#         "EUR": {
#             "code": "EUR",
#             "symbol": "&euro;",
#             "rate": "22,067.8331",
#             "description": "Euro",
#             "rate_float": 22067.8331
#         }
#     }
# }