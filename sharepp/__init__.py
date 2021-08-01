"""SharePriceProvider is a small application that provides the current price in EUR for a given ISIN."""
import requests

onvista_url = "https://www.onvista.de/"


def parse_price(isin):
    if isinstance(isin, str):
        response = requests.get(onvista_url + isin)
        price_string = response.text.split("ask")[1].split(":")[1].split(",")[0]
        return float(price_string)
    else:
        raise ValueError("You must provide a string object representing a valid ISIN!")
