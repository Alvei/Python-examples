""" state_table.py
    Gather simple infor on each US state.
"""
import re
import time
import dateutil.parser
import pandas as pd
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs
from typing import Optional

def get_url(url: str) -> str:
    """ Get the soup info from an url and do basic error checking. """
    try:
        response = requests.get(url)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'\n***HTTP error occurred: {http_err}')   # Python 3.6
    except Exception as err:
        print(f'\n***Other error occurred: {err}')       # Python 3.6
    return bs(response.text, features="lxml")

def to_date(date_str: str):
    """ Convert string to datetime. """
    date_str = re.match('[\w\s,]+', date_str)[0]
    return dateutil.parser.parse(date_str)

def to_int(number_str: str):
    """ Convert string to integer. """
    number_str = re.match('[\d,$]+', number_str)[0]
    number_str = number_str.replace('$', '').replace(',', '')
    return int(number_str)

def get_name(table):
    """ Get name of state embedded in table header. """
    raw_name = table.find('th').text
    return re.match('[A-z\s]+', raw_name)[0]

def get_date_admitted(table):
    """ Get admitted date to the union using word search. """
    raw_date = table.find(text='Admitted to the Union').next.text
    return to_date(raw_date)

def get_population(table):
    """ Get state population. """
    raw_population = table.find(text='Population')\
                        .parent.parent.next_sibling\
                        .find('td').text
    return to_int(raw_population)

def get_area(table):
    """ Get state area using regex. """
    raw_area = table.find(text=re.compile('Total')).next.text
    return to_int(raw_area)

def get_income(table):
    """ Get state area using regex. """
    raw_income = table.find(text='Median household income').next.next.text
    return to_int(raw_income)

def get_state_info(state_url: str) -> Optional[dict, None]:
    """ Gather basic info on a state. Does error checking for finding a table and finding a value. """
    try:
        # Use parse page and grab main table, raise exception if no table is found
        state_soup = get_url(state_url)
        state_table = state_soup.find('table')
    except:
        print(f"*** Cannot parse table: {state_url}")
        return None

    state_info = {}

    # Grab info with pre-defined functions
    # If any value can't be found, just fill value with None
    values = ['state', 'date_admitted', 'population',
            'area_sq_mi', 'median_household_income']
    functions = [get_name, get_date_admitted, get_population,
               get_area, get_income]

    for val, func in zip(values, functions):
        try:
            state_info[val] = func(state_table)
        except:
            state_info[val] = None

    return state_info

def main():
    """ Main script. """
    ny_url = 'https://en.wikipedia.org/wiki/New_York_(state)'

    ny_info = get_state_info(ny_url)
    print(ny_info)

    # Get the html info on
    list_url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States'
    list_soup = get_url(list_url)

    # Update 5/21/20 Table now first on page, switched from [1]
    # In the 1st table, find the table header and scope row
    state_rows = list_soup.find_all('table')[0].find_all('th', scope='row')
    # state_rows[0].find('a')
    # state_rows[0].find('a')['href']

    # Find the anchor link and extract the link
    state_links = [row.find('a')['href'] for row in state_rows]

    # Add the overall url
    base_url = 'https://en.wikipedia.org'
    state_urls = [base_url + link for link in state_links]
    # for link in state_urls:
    #     print(link)

    state_info_list = []

    for link in state_urls:

        state_info = get_state_info(link)
        if state_info:
            state_info_list.append(state_info)
        print(state_info['state'])
        # Be sure to pause
        time.sleep(1)

    # Convert the list of dictionary to a dataframe
    state_data = pd.DataFrame(state_info_list)
    print(state_data)

    state_data.to_csv('state_data.csv', index=False)

if __name__ == "__main__":
    main()