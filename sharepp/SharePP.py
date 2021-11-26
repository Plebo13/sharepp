import re

import requests
from bs4 import BeautifulSoup

LANG_UND_SCHWARZ_URL = "https://www.ls-tc.de/de/etf/"


def get_etf_price(isin: str) -> float:
    """
    Gets the current price of an ETF.
    :param isin: the ISIN of the ETF
    :return: the current price
    """
    if is_isin(isin):
        response = requests.get(LANG_UND_SCHWARZ_URL + isin)
        parsed_html = BeautifulSoup(response.text, "html.parser")
        price_span = parsed_html.find("div", class_="mono").find("span")
        price_string = price_span.text.replace(".", "").replace(",", ".")
        return float(price_string)
    else:
        raise ValueError("You must provide a string object representing a valid ISIN!")


def is_isin(isin: str) -> bool:
    if re.match("^[A-Za-z]{2}[A-Za-z0-9]{10}", isin):
        return True
    else:
        return False
