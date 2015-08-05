'''
1 - testing <tag list>.values
2 - roller coaster about miss understanding attributes, tags, learned a lot

ref:
    http://www.crummy.com/software/BeautifulSoup/bs4/doc/
    http://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI
# All your changes should be in the 'extract_carrier' function
# Also note that the html file is a stripped down version of what is actually on the website.

# Your task in this exercise is to get list of all airlines. Exclude all of the combination
# values, like "All U.S. Carriers" from the data that you return.
# You should return a list of codes for the carriers.

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_carriers(page):
    with open(html_page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        select = soup.find(id='CarrierList')
        carrier_options = select.find_all('option')
        carriers = [carrier['value'] for carrier in carrier_options][3:]
    return carriers


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': airport,
                          'CarrierList': carrier,
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

test()
