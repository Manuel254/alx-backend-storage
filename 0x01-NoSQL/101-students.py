#!/usr/bin/env python3
"""Returns all students sorted by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average
    score
    """
    return mongo_collection.aggregate(
            [{ "$unwind": "$topics" },
             { "$group": {
                "_id": "$_id",
                "averageScore": { "$avg": "$topics.score"},
                "name": {"$first": "$name" },
             }},
             { "$sort": {"averageScore": -1 }}])
