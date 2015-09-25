#!/usr/bin/env python
"""
Find the average regional city population for all countries in the cities collection.

What were asking here is that you first calculate the average city population for each region in a country and then calculate the average of all the regional averages for a country.

As a hint, _id fields in group stages need not be single values. They can also be compound keys (documents composed of multiple fields). You will use the same aggregation operator in more than one stage in writing this aggregation query. I encourage you to write it one stage at a time and test after writing each stage.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{'$match': {'name': {'$exists':1}}},
                {'$unwind': '$isPartOf'},
                {'$group': {'_id': '$isPartOf',
                            'country': {'$first':'$country'},
                            'avg': {'$avg': '$population'}}},
                {'$group': {'_id': '$country',
                            'avgRegionalPopulation': {'$avg': '$population'}}}]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

def init_func():
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result["result"]) < 150:
        pprint.pprint(result["result"])
    else:
        pprint.pprint(result["result"][:100])
    assert result["result"][0]["_id"] == 'Kuwait'
    assert result["result"][1]["avgRegionalPopulation"] == 363945.0
    assert result["result"][0] == {'_id': 'Kuwait', 'avgRegionalPopulation': 115945.66666666667}

if __name__ == '__main__':
    init_func()
