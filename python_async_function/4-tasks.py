#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple asynchronous tasks to wait for results of random delays.

    Args:
        n (int): The number of tasks to wait for.
        max_delay (int): The maximum delay time for each task.

    Returns:
        List[float]: A sorted list of the results of the tasks.
    """
    data = [task_wait_random(max_delay) for _ in range(n)]
    data = await asyncio.gather(*data)
    return sorted(data)
