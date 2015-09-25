#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


def fix_area(area):
    try:
        # assume it's a normal float string '52330000.0'
        return float(area)
    except:
        # split the 'list' format '{1.01787e+08|1.019e+08}'
        # take the first number from the list
        try:
            nums = area.split('|')
            nums = [nums[0][1:], nums[1][:-1]]
            if len(nums[0]) > len(nums[1]):
                num = nums[0]
            else:
                num = nums[1]
            return float(num)
        except:
            pass

def process_file(filename):
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        #skipping the extra matadata
        for i in range(3):
            next(reader)

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    # print ("Printing three example results:")
    for n in data:
        pprint.pprint(n["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None
    assert data[20]["areaLand"] == 14581600.0
    assert data[33]["areaLand"] == 20564500.0


if __name__ == "__main__":
    test()
