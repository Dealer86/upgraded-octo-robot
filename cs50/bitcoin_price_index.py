import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)
try:
    if (not sys.argv[1].isnumeric()) and (not float(sys.argv[1])):
        print("Command-line argument is not a number")
        sys.exit(1)
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)


def get_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(url)
    o = response.json()
    # print(o.keys())
    # print(o["bpi"])

    rate_float = float((o["bpi"]["USD"]["rate_float"]))

    currency = o["bpi"]["USD"]["code"]
    result = rate_float * float(sys.argv[1])
    p = f"{currency} {result:,.4f}"
    print(p)


get_bitcoin()
