import datetime

"""
Standard crypto model library classes for basic concepts like Currency, Prices and Orders (etc)
Useful guides to general Python class customisation:
https://docs.python.org/3/reference/datamodel.html#customization
https://realpython.com/blog/python/instance-class-and-static-methods-demystified/
"""

class FiatCurrency(object):
    isocode = "USD"
    symbol = "$"
    
    @classmethod
    def USD(cls):
        return cls("USD", "$")    
    
    """
    Used for a crypto currency
    Isocode is the 3 character currency code
    symbol is printable currency symbol (e.g. $)
    """
    def __init__(self, isocode, symbol):
        self.isocode = isocode
        self.symbol = symbol
        
    def __str__(self):
        return self.isocode


class CryptoCurrency(object):
    ticker = "BTC"
    website = ""
    
    @classmethod
    def BTC(cls):
        return cls("BTC")    

    @classmethod
    def EXCL(cls):
        return cls("EXCL")    
        
    @classmethod
    def getInstance(cls, ticker):
        return cls(ticker)
        
    """
    Used for a crypto currency
    ticker is the character ticker symbol
    website is the coin market cap url
    """
    def __init__(self, ticker):    
        self.ticker = ticker
        self.website = "http://www.coinmarketcap.com/" + ticker
        
    def __str__(self):
        return self.ticker

class CryptoCurrencyPair(object):
    base = ""
    curr = ""
    pair = ""
    website = ""
    
    @classmethod
    def getBtcPair(cls, ticker):
        return cls(CryptoCurrency.BTC(), CryptoCurrency.getInstance(ticker))
        
    @classmethod
    def getUsdBtcPair(cls):
        return cls(CryptoCurrency.BTC(), FiatCurrency.USD())
        
    """
    Used for a crypto currency trading pair
    Base is usually a mainstay base crypto currency like BTC or LTC
    Curr is the actual crypto currency to trade with 
    """
    def __init__(self, base, curr):
        self.base = base
        self.curr = curr
        self.pair = str(base) + "-" + str(curr)
        self.website = "https://www.bittrex.com/Market/Index?MarketName=" + self.pair
        
    def __str__(self):
        return str(self.pair)

class Price(object):
    currencypair = None
    price = None
    dateTimeStamp = None

    @classmethod
    def MISSING_PRICE(self):
        return float(-999999.99)
    
    """
    Used for a price
    """
    def __init__(self, currencypair, price):
        self.currencypair = currencypair
        self.price = price    
        self.dateTimeStamp = datetime.datetime.now()
        
    def __str__(self):
        return str(self.currencypair) + " " + str(self.price) + " " + str(self.dateTimeStamp)
        
class Order(object):
    depth = 0.0
    cryptoPrice = Price.MISSING_PRICE()
    fiatPrice = Price.MISSING_PRICE()
    quantity = 0.0
    depthQuantity = 0.0

    """
    Used for creating an order
    """
    def __init__(self, depth, cryptoPrice, quantity, depthQuantity):
        self.depth = depth
        self.cryptoPrice = cryptoPrice
        self.quantity = quantity
        self.depthQuantity = depthQuantity

    def __str__(self):
        return '%3i %14.8f %8.2f %14.2f %14.2f\n' % (self.depth, self.cryptoPrice, self.fiatPrice, self.quantity, self.depthQuantity)

    def priceFiat(self, fiatCryptoCurrencyPrice):
        self.fiatPrice = float(self.cryptoPrice) * float(fiatCryptoCurrencyPrice)
            
        
class OrderBook(object):
    cryptoCurrencyPair = None    
    orders = None
    
    """
    Used for storing a order book 
    """
    def __init__(self, cryptoCurrencyPair):
        self.cryptoCurrencyPair = cryptoCurrencyPair
        self.orders = []

    def addOrder(self, depth, cryptoPrice, quantity, depthQuantity):
        """
        Add specified Order object
        :param o: Order object to add
        :type o: Order
        """
        o = Order(depth, cryptoPrice, quantity, depthQuantity)
        self.orders.append(o)
        
    def priceFiat(self, fiatCryptoCurrencyPrice):
        for o in self.orders:
            o.priceFiat(fiatCryptoCurrencyPrice.price)

    def getPriceByQuantity(self, quantity):
        """
        Work out the exact average price that would be achieved by simply taking what is on offer for specified quantity
        For example if there are 100 @0.2, 200 @0.2, 100 @0.1 offered and specified quantity is 150 the average price would be 0.2
        :param q: Quantity 
        :type o: float
        :return: Average price for specified quantity 
        :rtype : Price
        """
        cost = 0.0
        for o in self.orders:
            cost = self.fiatPrice * self.quantity
        return 0.0
        
    def getFirstOrder(self):
        if (self.orders):
            return self.orders[0]

    def calcBestFiatPrice(self, fiatBasePrice, debug = False):
        if (self.orders):
            self.priceFiat(fiatBasePrice)
            bestprice = self.getFirstOrder().fiatPrice
            if (debug): print(bestprice)
            return bestprice
        return Price.MISSING_PRICE()
            
    def __str__(self):
        all = ""
        for o in self.orders:
            all += str(o)
        return all
        