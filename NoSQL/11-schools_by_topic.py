#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """return list having a specific topic

    Args:
        mongo_collection: collection
        topic: topics to specific

    Returns:
        return list with the specific topic
    """
    result = []
    cursor = mongo_collection.find({"topics": topic})
    for document in cursor:
        result.append(document)
    return result
