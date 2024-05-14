#!/usr/bin/env python3
"""
Script to provide statistics about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
    This function connects to the MongoDB instance and retrieves statistics
    about the Nginx logs stored in the 'logs.nginx' collection.

    The statistics include:
    - Total number of logs
    - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
    - Number of logs with method 'GET' and path '/status'
    """
    client = MongoClient()
    collection = client.logs.nginx

    total_logs = collection.count_documents({})

    method_counts = collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ])
    method_counts = {entry["_id"]: entry["count"] for entry in method_counts}

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = method_counts.get(method, 0)
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
