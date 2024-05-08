#!/usr/bin/env python3
"""
function make_multiplier that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """First function

    Args:
        multiplier (float)

    Returns:
        Callable[[float], float]
    """
    def muliplier_function(x: float) -> float:
        """Second function

        Args:
            x (float)

        Returns:
            float
        """
        return x * multiplier

    return muliplier_function
