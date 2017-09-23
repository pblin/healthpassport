"""
   Coinbase interaction API
   In future consider replacing this simple implementation with https://github.com/sibblegp/coinbase_python
   See also https://developers.coinbase.com/
"""

import time
import hmac
import hashlib
try:
    from urllib import urlencode
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urlencode
    from urllib.parse import urljoin
import requests
import re
from cryptomodel import Price
from cryptomodel import CryptoCurrencyPair

class Coinbase(object):

    BASE_URL = 'https://api.gdax.com/'
	
    """
    Used for scraping Coinbase home page (no API calls)
    """
    def api_query(self, method, options=None, debug = False):
        """
        Queries Coinbase with given method and options
        :param method: Query method for getting info
        :type method: str
        :param options: Extra options for query
        :type options: dict
        :return: JSON response from Bittrex
        :rtype : dict
        """
        if not options:
            options = {}
        nonce = str(int(time.time() * 1000))
        method_set = 'public'

        request_url = self.BASE_URL + method + '?'
        request_url += urlencode(options)
        if (debug): print(request_url)
        response = requests.get(request_url)
        return response.json()

    def getPrice(self, currencyPair, debug = False):
        """
        Used to scrape the btc to usd rate from the home page
        This is used as the actual currently machinable btc price
        :return: Available btc price in USD
        :rtype : float
        """
        dict = self.api_query('products/' + currencyPair.pair + '/ticker', debug = debug)
        if (debug): print(str(dict))
        btcprice = Price.MISSING_PRICE()
        if (dict and len(dict) > 1):
            btcprice = dict.get('price', Price.MISSING_PRICE())
            if (debug): print(btcprice)
        p = Price(currencyPair.pair, btcprice)
        return p
