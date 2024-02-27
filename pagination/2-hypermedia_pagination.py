#!/usr/bin/env python3
"""Write a function named index_range
that takes two integer arguments page and page_size"""
from typing import List, Dict
import csv
import math
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1
        and page_size with default value 10."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        start_index, end_index = index_range(page, page_size)
        res = self.dataset()
        return res[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """takes the same arguments (and defaults) as get_page
        and returns a dictionary"""
        totalpages = math.ceil(len(self.dataset()) / page_size)
        if page >= totalpages:
            nextp = None
        else:
            nextp = page + 1
        if page == 1:
            prevp = None
        else:
            prevp = page - 1
        data = self.get_page(page, page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": nextp,
            "prev_page": prevp,
            "total_pages": totalpages}
