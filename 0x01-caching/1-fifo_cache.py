#!/usr/bin/env python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class that inherits from Basecaching
    """
    def __init__(self):
        """
        Method that initializes 
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Method that add or updates an item in cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                first_key = self.keys.pop(0)
                del self.cache_data[first_key]
                print('DISCARD: {:s}'. format(first_key))

    def get(self, key):
        """
        Method that retrieves the cache data
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
