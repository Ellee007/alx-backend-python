#!/usr/bin/env python3
"""
This is our python3 module
"""
import asyncio
"""
This is async module
"""
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This is our function
    """
    return asyncio.create_task(wait_random(max_delay))
