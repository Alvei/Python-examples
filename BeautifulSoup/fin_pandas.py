""" fin_pandas.py
    Example using OOP to gather stok statistics.
    Inspired by
    https://medium.com/c%C3%B3digo-ecuador/python-web-scraping-stock-market-statistics-on-yahoo-finance-455929c835ed
    https://gist.github.com/dray89/46a982956d9667474e2cfcedf07406a0
    https://www.marsja.se/how-to-use-pandas-read_html-to-scrape-data-from-html-tables/
    It creates 10 tables.
    Missing a check to confirm that the stock is valid
    """

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests, lxml
from lxml import html
from datetime import date, datetime
import time


class statistics:
    base_url = "https://finance.yahoo.com/"  # Class attribute

    def __init__(self, symbol: str):
        """ symbol: stock symbol in all caps. Pls note that any Canadian TSX stocks are followed with ".TO"
            Define local class attributes specific to only that instance of the class object.
            Define callable attributes that list available public methods and attributes to improve the ease at
            which I use my self-written programs. Other class properties require the argument, symbol,
            to execute without throwing an error.
        """
        self.symbol = symbol.upper()
        self.path = "quote/{0}/key-statistics?p={0}".format(symbol)
        self.url = self.base_url + self.path
        self.methods = ["scrape_page", "label_stats"]
        self.attributes = [
            "self.symbol",
            "self.path",
            "self.url",
            "self.methods",
            "self.hdrs",
            "self.valuation",
            "self.fiscal_year",
            "self.profitability",
            "self.manager_effect",
            "self.income_statement",
            "self.balance_sheet",
            "self.cash_statement",
            "self.price_history",
            "self.share_stats",
            "self.dividendSplit",
        ]
        self.hdrs = {
            "authority": "finance.yahoo.com",
            "method": "GET",
            "path": self.path,
            "scheme": "https",
            "accept": "text/html,application/xml;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "referer": self.base_url,
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0;)",
        }  # To be used by headers during .get()

    def scrape_page(self):
        """ Scrapes the content of the class URL, using headers defined in the init function,
            returns a byte string of html code.
        """
        page = requests.get(
            self.url, headers=self.hdrs
        )  # Get the content from the urls
        soup = BeautifulSoup(page.content, "lxml")  # Convert into BS4 content
        tables = soup.find_all("table")  # Find all the tables on the page
        iterator = range(0, len(tables))

        # pd.read_html() reads the html tables on the website.
        # By entering the text from x as as string it reads that specific table
        function = lambda x: pd.read_html(str(tables[x]))

        # map() expects a function object and an iterable and returns an iterator or map object.
        # Use list() to convert to list of list. Each element is a pd
        table_list = list(map(function, iterator))

        return table_list

    def label_stats(self, table_list):
        """ :param table_list: uses the output of the scrape_page method
            :return: creates attributes for the statistics class object,
                     uses indexLabel method to label columns and set the dataframes' index
            label_stats method will use the special __indexLabel__ operation within the
            lambda function to label and index quickly all 10 of our tables.
        """

        # iterator is a list of 10 dataframe representing the 10 tables. Index is number
        iterator = [table_list[i][0] for i in range(0, len(table_list))]
        # for i in iterator:
        #     print(f"{i}\n")

        # Apply __indexLabel__(df) to each of the 10 dataframes
        table_list = list(map(lambda df: self.__indexLabel__(df), iterator))

        # Assign the 10 df to object attributes
        # self.valuation, self.fiscal_year, self.profitability, self.manager_effect, \
        # self.income_statement, self.balance_sheet, self.cash_statement, \
        # self.price_history, self.share_stats, self.dividendSplit = table_list

        return table_list

    def __indexLabel__(self, df):
        """ :param df: Takes a dataframe as input.
            :return: returns a dataframe with column labels and a set index.
        """
        shape = df.shape
        # print(df.shape)  # Shows that all tables have 2 columns except the 1st one that has 7

        if shape[1] == 2:  # Create a df with the two columns
            df.columns = ["Measure", "Value"]
        else:  # It is the big dataframe with 7 column
            current = df.columns[1]
            # print(current) # Get today's date
            df.rename(
                columns={
                    "Unnamed: 0": "Measure",
                    current: date.today().strftime("%m/%d/%Y"),
                },
                inplace=True,
            )

        df = df.set_index("Measure")  # Convert the Measures column into the index
        # print(df.columns)

        return df


def ticker_to_excel(stock_name, table_list):
    """ Save in excel the table. """
    print(f"Saving {stock_name} to Excel")
    table_names = [
        "Valuation",
        "Hist",
        "Share",
        "Div",
        "FY",
        "Profit",
        "Eff",
        "P&L",
        "BS",
        "CF",
    ]

    filename = stock_name + ".xlsx"
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(filename, engine="xlsxwriter")

    for i, p in enumerate(table_list):
        print(i, p)
        p.to_excel(writer, sheet_name=table_names[i])

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()


def get_SP500() -> list:
    """ Get list of ticker symbols for S&P500. """
    try:
        # Downloaded the file from https://datahub.io/core/s-and-p-500-companies#data
        filename = "constituents_csv.csv"
        SP500_df = pd.read_csv(filename)
        SP500_temp = SP500_df.Symbol.tolist()  # Get the symbols and save as a list
        SP500 = [
            x.replace(".", "-") for x in SP500_temp
        ]  # Use list comprehension to replace '.' with '-'
        print(SP500)
        return SP500
    except IOError:
        print(f"***Could not read: {filename}")


if __name__ == "__main__":
    price_book = []
    price_sales = []
    PE = []

    stocks = [
        "acn",
        "adbe",
        "adi",
        "adm",
        "adp",
        "a",
        "aa",
        "aapl",
        "abbv",
        "abc",
        "abt",
        "MSFT",
    ]
    FANG = ["FB", "AAPL", "NFLX", "GOOGL"]
    Tech = FANG + ["IBM", "MSFT", "DELL", "CRM", "ABDE"]
    SP500 = get_SP500()

    stocks = ["IPS.PA"]
    print("*****NEW********")
    """ for stock in stocks:
        stock_stats = statistics(stock)
        print(f"Stock: {stock_stats.symbol}")
        table_list = stock_stats.scrape_page()
        # print(f"\nNumber of tables: {len(table_list)}")  # There are ten tables


        table_list = stock_stats.label_stats(table_list)
        # for table in table_list:
        #     print("\n")
        #     print(table)

        df = table_list[0]  # the table with key stats
        #print(df)
        price_book.append(float(df.loc['Price/Book (mrq)'][0]))
        price_sales.append(float(df.loc['Price/Sales (ttm)'][0]))
        PE.append(float(df.loc['Trailing P/E'][0]))
        time.sleep(1)

    DF = pd.DataFrame({"Stock": stocks, "PE": PE, "P/S": price_sales, "P/B": price_book})
    print(DF) """

# tock_stats = statistics('MSFT')
stock_stats = statistics("IPS.PA")
print(f"Stock: {stock_stats.symbol}")
table_list = stock_stats.scrape_page()
# print(f"\nNumber of tables: {len(table_list)}")  # There are ten tables

table_list = stock_stats.label_stats(table_list)
for p in table_list:
    print(f"\n{p}")

# ticker_to_excel(stock_stats.symbol, table_list)

