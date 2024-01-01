#!/usr/bin/env python3

"""
function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a string and an int or float to a tuple.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        A tuple containing the string k and the square of v as a float.
    """
    result = (k, float(v)**2)
    return result
