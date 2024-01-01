#!/usr/bin/env python3
"""
function make_multiplier that takes a
float multiplier as argument and
returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates and returns a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        A function that multiplies a float by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
