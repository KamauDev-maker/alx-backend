#!/usr/bin/env python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class that inherits Basecaching
    """
    def __init__(self):
        """
        Method that initializes class instance
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Method that adds or updates the a cached item
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.keys.pop(0)
                del self.cache_data[lru_key]
                print('DISCARD: {:s}'.format(lru_key))

    def get(self, key):
        """
        Method that retrieves an item from cache
        """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
