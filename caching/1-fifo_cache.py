#!/usr/bin/env python3
""" BaseCaching module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' A basic cache.
        Inherits from class BaseCaching.
        Attributes:
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache
    '''

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' Add key/value pair to cache.
        If either `key` or `item` is None, do nothing. '''
        if (key is None or item is None):
            return
        if len(self.cache_data) >= super().MAX_ITEMS:

            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f'DISCARD: {first_key}')

        self.cache_data[key] = item

    def get(self, key):
        ''' Return value stored in `key` of cache.
        If key is None or does not exist in cache, return None. '''
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
