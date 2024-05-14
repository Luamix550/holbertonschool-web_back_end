#!/usr/bin/env python3
"""
Python function that inserts a new document in
a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    insert_d = mongo_collection.insert_many(kwargs)
    return insert_d.inserted_id
