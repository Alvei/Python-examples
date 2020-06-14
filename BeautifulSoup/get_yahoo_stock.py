""" From Ery Lewinson medium: A comprehensive guide to downloading stock price in Python.
https://aroussi.com/post/python-yahoo-finance
https://github.com/ranaroussi/yfinance """

import pandas as pandas
import yfinance as yf
import matplotlib.pyplot as plt
import sys
def pretty_print(stock):
    for key in stock:
        print(f"{key}: {stock[key]}")
def main(argv):
    # from yahoofinancials import yahoofinancials
    # tsla_df = yf.download('TSLA', start='2019-01-01', end='2019-12-31', progress=False)
    # print(tsla_df.head())
    print(f"len {len(sys.argv)}")
    if len(sys.argv) == 2:
        stock = sys.argv[1].upper()
    else:
        stock = 'SPY'

    print(f"Getting data for {stock}")
    ticker = yf.Ticker(stock)
    stock_df = ticker.history(period="max")
    msg = str(stock) + "'s stock Price"
    stock_df['Close'].plot(title=msg)
    plt.show()
    #pretty_print(ticker.info)
    #print(f"Major Shareholders: {ticker.institutional_holders}")


    #yahoo_financials = YahooFinancials('TSLA')

if __name__ == "__main__":
    main(sys.argv[1:])