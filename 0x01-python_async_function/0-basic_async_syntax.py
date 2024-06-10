#!/usr/bin/env python3
"""
This is our module
"""
import asyncio
import random
"""
This is asyncio, random module
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    This is wait_random function
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
