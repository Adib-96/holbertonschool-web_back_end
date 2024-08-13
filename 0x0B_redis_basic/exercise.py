#!/usr/bin/env python3
'''
Python module to communicate with Redis server
'''
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        '''
        Connect to the Redis server and flush the database
        '''
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Generate a random key
        '''
        key = str(uuid.uuid4())

        self._redis.set(key, data)

        return key

