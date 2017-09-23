import unittest
import json
from coinbase import Coinbase

class TestCoinbaseHomePage(unittest.TestCase):
    """
    Integration tests for the Coinbase home page
    These will fail in the absence of an internet connection or if coinbase goes down
    """
    def setUp(self):
        self.coinbase = Coinbase()

    def test_getBtcPrice(self):
        actual = self.coinbase.getBtcPrice()
        print(actual)
        self.assertTrue( actual != -1, "result is not found")
        self.assertTrue( actual > 100.0, "result is a number less than 100")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCoinbaseHomePage)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)