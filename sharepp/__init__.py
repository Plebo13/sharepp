"""SharePriceProvider is a small application that provides the current price in EUR for a given ISIN."""
import requests

ONVISTA_URL = "https://www.onvista.de/"


def parse_price(isin):
    if isinstance(isin, str):
        response = requests.get(ONVISTA_URL + isin)
        price_string = response.text.split("ask")[1].split(":")[1].split(",")[0]
        return float(price_string)
    else:
        raise ValueError("You must provide a string object representing a valid ISIN!")
