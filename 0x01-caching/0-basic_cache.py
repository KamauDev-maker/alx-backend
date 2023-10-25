#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    """
    def put(self, key, item):
        """
        Method used to add or update an item and takes two params
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Method usd to retrieve an item
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
