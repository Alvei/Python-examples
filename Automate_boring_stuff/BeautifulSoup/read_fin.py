""" yscrap.py
    Inspired by Sentdex
    https://www.youtube.com/watch?v=K2zyPby4034&list=PLQVvvaa0QuDejNczz7dbpyu3JnwUBvNch&index=3 """



import time
import urllib

def y_key_stat(stock: str) -> None:
    """ Get key stats on a stock. """
    url = 'https://finance.yahoo.com/quote/MSFT/key-statistics?p=MSFT'
    try:
        source = urllib.request.urlopen(url).read()
    except Exception as e:
        print(f"Could not open the website {url} {e}")
