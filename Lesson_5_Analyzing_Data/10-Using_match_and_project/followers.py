#!/usr/bin/env python
"""
Write an aggregation query to answer this question:

Of the users in the "Brasilia" timezone who have tweeted 100 times or more,
who has the largest number of followers?

The following hints will help you solve this problem:
- Time zone is found in the "time_zone" field of the user object in each tweet.
- The number of tweets for each user is found in the "statuses_count" field.
  To access these fields you will need to use dot notation (from Lesson 4)
- Your aggregation query should return something like the following:
{u'ok': 1.0,
 u'result': [{u'_id': ObjectId('52fd2490bac3fa1975477702'),
                  u'followers': 2597,
                  u'screen_name': u'marbles',
                  u'tweets': 12334}]}
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [{'$match':{'user.time_zone': 'Brasilia',
                           'user.statuses_count': {'$gte': 100 }}},
                {'$project': {'followers': "$user.followers_count",
                              'screen_name': '$user.screen_name',
                              'tweets': '$user.statuses_count'}},
                {'$sort': {"followers": -1}},
                {'$limit': 1}]
    return pipeline

def aggregate(db, pipeline):
    result = db.tweets.aggregate(pipeline)
    return result

def init_func():
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 1
    # assert result["result"][0]["followers"] == 17209
    import pprint
    pprint.pprint(result['result'][0]["followers"])

if __name__ == '__main__':
    init_func()
