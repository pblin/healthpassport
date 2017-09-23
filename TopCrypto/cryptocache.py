from coinbase.coinbase import Coinbase
from bittrex.bittrex import Bittrex
from cryptomodel import CryptoCurrencyPair
from cryptomodel import Price

"""
Higher level caching classes constructed using the individual exchange classes (e.g. Bittrex & Coinbase)
and the standard crypto model library classes (cryptomodel)
"""

class PriceCache(object):
    coinbase = None
    bittrex = None
    tickerlist = None
    cache = None
    """
    A pricing cache
    """
    def __init__(self, tickerlist):
        self.coinbase = Coinbase()
        self.bittrex = Bittrex(None, None)
        self.tickerlist = tickerlist
        self.cache = {}
        
    def __str__(self):
        return str(self.cache)

    def populate(self, debug = True):

        # Fetch base fiat price
        btcprice = self.coinbase.getPrice(CryptoCurrencyPair.getUsdBtcPair(), debug)
        self.cache["BTC"] = btcprice.price

        # Get a fiat price in USD for every ticker
        for ticker in self.tickerlist:
            orderbook = self.bittrex.getOrderBook(CryptoCurrencyPair.getBtcPair(ticker), Bittrex.BUY_ORDERBOOK, 50, debug)
            bestprice = orderbook.calcBestFiatPrice(btcprice, debug = True)
            self.cache[ticker] = bestprice
            if (debug): print("populate(): Adding " + ticker + " with price " + str(bestprice))
        
        # Print results
        if (debug): print(str(self.cache))
            
    def getPrice(self, ticker):
        return cache.get(ticker, Price.MISSING_PRICE())

    def getValuation(self, quantity):
        return self.getPrice(ticker) * float(quantity)
        