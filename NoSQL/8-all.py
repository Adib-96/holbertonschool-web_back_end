#!/usr/bin/env python3
""" Write a Python function that lists all documents in a collection """


def list_all(mongo_collection):
    '''Python function that lists all documents in a collection'''
    documents = mongo_collection.find()
    if documents.count() == 0:
        return []
    return documents
