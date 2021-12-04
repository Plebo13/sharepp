import unittest

from sharepp import SharePP, Coin


class SharePPTest(unittest.TestCase):

    def test_valid_stock_input(self):
        price = SharePP.get_etf_price("US0378331005")
        self.assertTrue(float, type(price))

    def test_valid_etf_input(self):
        price = SharePP.get_etf_price("LU1781541179")
        self.assertTrue(float, type(price))

    def test_invalid_input(self):
        try:
            SharePP.get_etf_price("invalid_isin")
            self.fail("Expected exception not thrown!")
        except ValueError as e:
            self.assertEqual(
                "You must provide a string object representing a valid ISIN!",
                str(e))

    def test_get_coin_price(self):
        for coin in Coin:
            price = SharePP.get_coin_price(coin)
            self.assertTrue(float, type(price))


if __name__ == '__main__':
    unittest.main()
