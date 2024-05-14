#!/usr/bin/env python3
"""
Python function that inserts a new document in
a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new school document into a MongoDB collection.

    Args:
        mongo_collection: A pymongo collection object.
        **kwargs: Keyword arguments representing the fields
        and values of the school document to be inserted.

    Returns:
        The ObjectId (_id) of the newly inserted school document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
