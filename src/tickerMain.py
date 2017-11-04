import greetingsText
from pycoincap import CryptoMarket as market



if __name__ == "__main__":
    timedate_obj = greetingsText.TimeDate()
    print(timedate_obj.get_time())
    print(timedate_obj.get_date())
    print(timedate_obj.get_greetings())
    m = market()
    b = m.coin('Bitcoin')
    print(b)


    
