from time import sleep
import unittest

import sharepp


class SharePPTest(unittest.TestCase):

    def test_valid_stock_input(self):
        price = sharepp.get_stock_price("US0378331005")
        self.assertTrue(float, type(price))

    def test_valid_etf_input(self):
        price = sharepp.get_etf_price("LU1781541179")
        self.assertTrue(float, type(price))

    def test_invalid_input(self):
        try:
            sharepp.get_etf_price("invalid_isin")
            self.fail("Expected exception not thrown!")
        except ValueError as e:
            self.assertEqual(
                "You must provide a string object representing a valid ISIN!", str(e)
            )

    def test_get_coin_price(self):
        price = sharepp.get_coin_price(sharepp.Coin.BITCOIN)
        self.assertTrue(float, type(price))
        sleep(5)


if __name__ == "__main__":
    unittest.main()
