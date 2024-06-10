#!/usr/bin/env python3
"""
This is our python module
"""
import asyncio
from typing import List
"""
These are typing, asyncio and random modules
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is our function
    """
    i: int = 0
    delay_list: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task_result in asyncio.as_completed(tasks):
        delay_list.append(await task_result)
    return delay_list
