#!/usr/bin/env python3
"""
Hypermedia Pagnition
"""
from typing import List, Tuple, Dict
import csv
from math import ceil


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the pagination
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary
        """
        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        total_pages: int = len(dataset) if dataset else 0
        total_pages = ceil(total_pages / page_size)
        prev_pages: int = (page - 1) if (page - 1) >= 1 else None
        next_pages: int = (page + 1) if (page + 1) <= total_pages else None
        hypermedia: Dict = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_pages,
                'prev_page': prev_pages,
                'total_pages': total_pages,
        }
        return hypermedia
