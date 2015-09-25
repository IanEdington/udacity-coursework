#!/usr/bin/env python
"""
The tweets in our twitter collection have a field called "source". This field describes the application
that was used to create the tweet. Following the examples for using the $group operator, your task is
to modify the 'make-pipeline' function to identify most used applications for creating tweets.
As a check on your query, 'web' is listed as the most frequently used application.
'Ubertwitter' is the second most used.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, the aggregation
pipeline should be a list of one or more dictionary objects.

import twitter dataset with:
    mongoimport --db twitter --collection tweets --file twitter.json
"""


def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
            {"$group": {'_id': '$source',
                       'count': {'$sum':1}}},
            {"$sort": {'count': -1}}]
    return pipeline

def tweet_sources(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

# Script Function
def init_func():
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = tweet_sources(db, pipeline)
    import pprint
    pprint.pprint(result)

if __name__ == '__main__':
    init_func()
