#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
from pprint import pprint
from collections import defaultdict

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]

def audit_file(filename, fields):
    fieldtypes = defaultdict(set)
    fieldvalues = defaultdict(set)

    f = open(filename, 'r')
    reader = csv.DictReader(f)
    header = reader.fieldnames

    # skip firt 3 lines of header info
    reader.next()
    reader.next()
    reader.next()

    # loop through each row checking each field we care about
    for row in reader:
        for field in fields:
            cell = row[field]
            if (cell == "NULL") | (cell == ""):
                celltype = type(None)
            elif cell[0:1] == "{":
                type([])
            else:
                try:
                    cell = int(cell)
                    celltype = type(1)
                except:
                    try:
                        cell = float(cell)
                        celltype = type(1.1)
                    except:
                        celltype = type('string')

            fieldtypes[field] |= {celltype}
            fieldvalues[field] |= {cell}

    pprint(fieldtypes)
    pprint(fieldvalues)

    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
