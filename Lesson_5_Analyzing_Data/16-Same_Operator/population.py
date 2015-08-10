#!/usr/bin/env python
"""
In an earlier exercise we looked at the cities dataset and asked which region in India contains the most cities. In this exercise, we'd like you to answer a related question regarding regions in India. What is the average city population for a region in India? Calculate your answer by first finding the average population of cities in each region and then by calculating the average of the regional averages.

Hint: If you want to accumulate using values from all input documents to a group stage, you may use a constant as the value of the "_id" field. For example,
    { "$group" : "India Regional City Population Average",
      ... }

"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{'$match': {"country" : "India"}},
                {'$unwind': '$isPartOf'},
                {'$group': {'_id': '$isPartOf',
                            'avg_pop': {'$avg': '$population'}}},
                {'$group': {'_id': "India Regional City Population Average",
                            'avg': {'$avg': '$avg_pop'}}}]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

def init_func():
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 1
    assert result["result"][0]["avg"] == 196025.97814809752
    import pprint
    pprint.pprint(result)

if __name__ == '__main__':
    init_func()
