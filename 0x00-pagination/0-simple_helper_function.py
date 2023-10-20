#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Method that takes two int and returns a tuple
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
