""" YouTube Link: https://www.youtube.com/watch?v=87Gx3U0BDlo

    Ensure that you have both beautifulsoup and requests installed:
    pip install beautifulsoup4
    pip install requests """
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

## Statistics to pull from Yahoo Finance "Key Statistcs" Page i.e. http://finance.yahoo.com/q/ks?s=YHOO+Key+Statistics
keyStatistics = [
	"Trailing P/E",
	"Forward P/E",
	"Revenue (ttm)",
	"EBITDA (ttm)",
	"Total Cash (mrq)",
	"Total Debt (mrq)",
	"Forward Annual Dividend Yield",
	"Payout Ratio",
	"52-Week Change",
	"Short % of Float ",
]


def y_currency() -> None:
    """ Get currency data. """
    url = 'https://finance.yahoo.com/currencies'
    names=[]
    prices=[]
    changes=[]
    percentChanges=[]
    marketCaps=[]
    totalVolumes=[]
    circulatingSupplys=[]

    result = requests.get(url)
    result.raise_for_status()

    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    #counter = 40
    for i in range(40, 404, 14):
        for listing in soup.find_all('tr', attrs={'data-reactid':i}):
            for name in listing.find_all('td', attrs={'data-reactid':i+3}):
                names.append(name.text)
            for price in listing.find_all('td', attrs={'data-reactid':i+4}):
                prices.append(price.text)
            for change in listing.find_all('td', attrs={'data-reactid':i+5}):
                changes.append(change.text)
            for percentChange in listing.find_all('td', attrs={'data-reactid':i+7}):
                percentChanges.append(percentChange.text)
    df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
    print(df)


def main():
    y_currency()

if __name__ == "__main__":
    print(f"\n Gathering Financial Data....")
    main()