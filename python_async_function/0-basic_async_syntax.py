#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay between 0
and max_delay seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Write an asynchronous coroutine 

    Args:
        max_delay (int, optional)

    Returns:
        float
    """
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
