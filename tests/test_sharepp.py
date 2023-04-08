import unittest
import sharepp


class SharePPTest(unittest.TestCase):
    def test_valid_input(self):
        price = sharepp.get_etf_price("LU1781541179")
        self.assertTrue(float, type(price))

    def test_invalid_input(self):
        with self.assertRaises(ValueError) as e:
            sharepp.get_etf_price("invalid_isin")
            self.assertEqual(
                "You must provide a string object representing a valid ISIN!",
                str(e.exception),
            )

    def test_get_coin_price(self):
        for coin in sharepp.Coin:
            price = sharepp.get_coin_price(coin)
            self.assertTrue(float, type(price))


if __name__ == "__main__":
    unittest.main()
