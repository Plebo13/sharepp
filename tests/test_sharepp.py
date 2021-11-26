import unittest
from sharepp import SharePP
from sharepp.Coin import Coin


class TestSharePP(unittest.TestCase):

    def test_valid_input(self):
        price = SharePP.get_etf_price("IE00BHZPJ569")
        self.assertTrue(float, type(price))

    def test_invalid_input(self):
        try:
            SharePP.get_etf_price("invalid_isin")
            self.fail("Expected exception not thrown!")
        except ValueError as e:
            self.assertEqual("You must provide a string object representing a valid ISIN!", str(e))

    def test_get_coin_price(self):
        price = SharePP.get_coin_price(Coin.BITCOIN)
        print(str(price))
        self.assertTrue(float, type(price))


if __name__ == '__main__':
    unittest.main()
