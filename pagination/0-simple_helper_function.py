#!/usr/bin/env python3
"""
    Calculate the start and end indices for a given page and page size.

    Args:
    - page (int): The page number (1-indexed).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start index and end index for the specified page.
"""


def index_range(page, page_size) -> tuple[int, int]:
    ''' Return tuple containing pagination start index and end index. '''
    return ((page_size * (page - 1)), page_size * page)
