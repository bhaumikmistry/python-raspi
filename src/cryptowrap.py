from pycoincap import CryptoMarket as market

"""
Api to get data from 
Retrieve informations from https://coinmarketcap.com/

The location for the source code
https://github.com/ZoranPandovski/pycoincap
"""

class Cryptowrap:
    """
    class to get current price
    later to get other informations
    """
    def __init__(self):
        self.m = market()
        self.bit_obj = self.m.coin('bitcoin') 
        self.eth_obj = self.m.coin('ethereum')
        self.lit_obj = self.m.coin('litecoin')

    def getBitcoin(self,currency):
        if currency.upper() == "USD":
            return self.bit_obj.price_usd

    def getEthereum(self,currency):
        if currency.upper() == "USD":
            return self.eth_obj.price_usd

    def getLitcoin(self,currency):
        if currency.upper() == "USD":
            return self.lit_obj.price_usd
            
        return self.lit_obj.price_usd

# if __name__ == "__main__":
#     cry = Cryptowrap()
#     print(cry.getBitcoin('usd'))
#     print(cry.getEthereum('usd'))
#     print(cry.getLitcoin('usd'))

