#!/usr/bin/env python3
'''
Python module to communicate with Redis server
'''
import redis
import uuid
from typing import Union, Optional, Callable, Any


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

    def get(self, key, fn: Optional[Callable[[bytes], Any]]) -> Any:
        """Retrieves a value from Redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Retrieves a value from Redis and converts it to a string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieves a value from Redis and converts it to an integer."""
        return self.get(key, fn=int)
