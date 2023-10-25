#!/usr/bin/env python3
"""
LIFO cache
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    """
    def __init__(self):
        """
        Method that initializes class instance
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Method that add or updates a cache items
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.keys.pop(-2)
                del self.cache_data[last_key]
                print('DISCARD: {:s}'.format(last_key))

    def get(self, key):
        """
        Method that retrieves a cache item
        """
        if key is not None:
            return self.cache_data[key]
        return None
