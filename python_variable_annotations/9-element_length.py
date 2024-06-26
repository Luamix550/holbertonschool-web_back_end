#!/usr/bin/env python3
"""
function’s parameters and return values with the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function’s parameters and return values
    with the appropriate types

    Args:
        lst (Iterable[Sequence])

    Returns:
        List[Tuple[Sequence, list]]
    """
    return [(i, len(i)) for i in lst]
