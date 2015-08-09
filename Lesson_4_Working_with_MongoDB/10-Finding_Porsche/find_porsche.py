#!/usr/bin/env python
"""
Your task is to complete the 'porsche_query' function and in particular the query
to find all autos where the manufacturer field matches "Porsche".
Please modify only 'porsche_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB and download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials at
the following link:
https://www.udacity.com/wiki/ud032

Importing data to MongoDB
    in the terminal from the Data_Sets folder import autos.csv using the following command
    mongoimport --db examples --collection autos --type csv --file autos.csv --headerline
"""

import pymongo
from pymongo import MongoClient
import csv
from pprint import pprint

def get_db(db_name):
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche
    query = {"manufacturer" : "Porsche"}
    return query

def find_porsche(db, query):
    return db.autos.find(query)

if __name__ == "__main__":
    db = get_db('examples')
    query = porsche_query()
    p = find_porsche(db, query)

    for a in db.autos.find({}, {'manufacturer': 1}).limit(10):
        pprint(a)
