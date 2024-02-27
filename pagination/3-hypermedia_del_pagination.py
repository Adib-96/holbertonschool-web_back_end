#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import Dict, List

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia index based on the provided index and page_size."""
        assert index is None or (isinstance(index, int) and index >= 0), "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.indexed_dataset()

        # Calculate the current index and next index
        current_index = index if index is not None else 0
        next_index = current_index + page_size

        # Ensure the current index is within a valid range
        assert current_index < len(dataset), "Index out of range"

        # Get the data for the current page
        data = [dataset[i] for i in range(current_index, min(next_index, len(dataset)))]

        return {
            'index': current_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
