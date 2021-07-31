import sys
import requests

onvista_url = "https://www.onvista.de/"


def parse_price(isin):
    if isinstance(isin, str):
        response = requests.get(onvista_url + isin)
        price_string = response.text.split("ask")[1].split(":")[1].split(",")[0]
        return float(price_string)
    else:
        raise ValueError("You must provide a string object representing a valid ISIN!")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("You must provide exactly one argument.")
    else:
        print(parse_price(sys.argv[1]))
