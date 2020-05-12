"""test_parse_dates.py """
import pytest
import datetime
import sys, os
# required to allow to find the file to test in directory above the test directory
"""myPath = os.path.dirname(os.path.abspath(__file__))
print(myPath)
sys.path.insert(0, myPath + '\\..\\Chapter_6-Manipulating_Strings\\') """
from Parse_dates import try_parsing_date

@pytest.mark.parametrize('date, result',[
    ('2020-05-18', datetime.datetime(2020, 5, 18)),
    ('18.5.2014', datetime.datetime(2014, 5, 18)),
    ('18/05/2019', datetime.datetime(2019, 5, 18)),
])
def test_try_parsing_date_good(date, result):
    """check that the entered data is correct"""
    assert try_parsing_date(date) == result

@pytest.mark.parametrize('date, result',[
    ('2020+05-18', False),
    ('33-5-2014', False),
    ('18-15-2019', False),
    ('xx-xx-xxxx', False),
    ('xxx', False)
])
def test_try_parsing_date_bad(date, result):
    """check that the entered data is correct"""
    assert try_parsing_date(date) == result


