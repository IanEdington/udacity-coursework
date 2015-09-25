#!/usr/bin/env python
"""
$push is similar to $addToSet. The difference is that rather than accumulating only unique values it aggregates all values into an array.

Using an aggregation query,
1. count the number of tweets for each user
2. In the same $group stage, use $push to accumulate all the tweet texts for each user.
3. Limit your output to the 5 users with the most tweets.

Your result documents should include only the fields:
    "_id" (screen name of user),
    "count" (number of tweets found for the user),
    "tweet_texts" (a list of the tweet texts found for the user).
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{'$group':{'_id': '$user.screen_name',
                           'count': {'$sum':1},
                           'tweet_texts': {'$push': '$text'}}},
                {'$sort': {'count': -1}},
                {'$limit': 5}]
    return pipeline

def aggregate(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

def init_func():
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 5
    assert result["result"][0]["count"] > result["result"][4]["count"]
    import pprint
    pprint.pprint(result)

if __name__ == '__main__':
    init_func()
