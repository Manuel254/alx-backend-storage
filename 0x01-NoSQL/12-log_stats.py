#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in db"""


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    data = client.logs.nginx

    print(data.count_documents({}), "logs")
    print("Methods:")

    get = data.count_documents({"method": "GET"})
    post = data.count_documents({"method": "POST"})
    put = data.count_documents({"method": "PUT"})
    patch = data.count_documents({"method": "PATCH"})
    delete = data.count_documents({"method": "DELETE"})

    print("\tmethod GET: {}".format(get))
    print("\tmethod POST: {}".format(post))
    print("\tmethod PUT: {}".format(put))
    print("\tmethod PATCH: {}".format(patch))
    print("\tmethod DELETE: {}".format(delete))

    status = data.count_documents({"method": "GET", "path": "/status"})
    print(status, "status check")
