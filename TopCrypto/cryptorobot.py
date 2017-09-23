"""
Crypto Robot entry point

This module is intended to have high level logic for control pricing and trading functions.
This detail of interacting with exchanges (such as Bittrex and Coinbase) is abstracted using standard class modules.
"""

from cryptocache import PriceCache

priceCache = PriceCache([ "PIVX", "DCR", "EXCL", "CRW", "XMR" ])
priceCache.populate(debug = True)
