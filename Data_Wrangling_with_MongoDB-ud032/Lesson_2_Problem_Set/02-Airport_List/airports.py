'''
1 - use carriers as base. Because list is not in order it doesn't work to chop off fisrt 3
2 - use sets to chop off unwanted values

ref:
    https://docs.python.org/2/library/stdtypes.html#set
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"
page = html_page

def extract_airports(page):
    with open(page, "r") as html:
        soup = BeautifulSoup(html)
        airport_options = soup.find(id='AirportList').find_all('option')
        airports = set(airport['value'] for airport in airport_options)
        airports -= set(['AllMajors', 'All', 'AllOthers'])
    return airports

def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
