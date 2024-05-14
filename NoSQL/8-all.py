#!/usr/bin/env python3
"""
Python function that lists all documents in a collection
"""

import pymongo


def list_all(mongo_collection):
    """List all documents

    Args:
        mongo_collection: Collection

    Returns:
        Return empy list if not documents in collection
    """
    documents = []
    for document in mongo_collection.find():
        documents.append(document)
    return documents
