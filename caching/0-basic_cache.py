#!/usr/bin/env python3
"""
BaseCaching module representing how to save data and
manipulate it frm the cache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
        Add an item in the cache :)
        """
        if (key is None or item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
