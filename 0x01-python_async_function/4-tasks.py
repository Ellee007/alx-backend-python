#!/usr/bin/env python3
"""
This is our python module
"""
import asyncio
from typing import List
"""
These are typing, asyncio and random modules
"""
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is our function
    """
    delay_list: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task_result in asyncio.as_completed(tasks):
        delay_list.append(await task_result)
    return delay_list
