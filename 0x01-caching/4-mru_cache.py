#!/usr/bin/env python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    """
    def __init__(self):
        """
        Method that initializes the class instance
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Method that adds or updates the cached key and item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.keys.pop(-2)
                del self.cache_data[mru_key]
                print('DISCARD: {:s}'.format(mru_key))

    def get(self, key):
        """
        Method that retrieves cached item
        """
        if key is not None:
            if key in self.cache_data:
                return self.cache_data[key]
        return None
