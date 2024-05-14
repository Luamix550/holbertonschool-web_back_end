#!/usr/bin/env python3
"""
Python function that changes all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """Update all topics based on the name

    Args:
        mongo_collection: Collection to change topics
        name: filter to cahnge the topic
        topics: to change

    Returns:
        return changes
    """
    update_name = {"name": name}
    update_topics = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(update_name, update_topics)
    return result
