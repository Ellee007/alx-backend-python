#!/usr/bin/env python3
"""
This is our module
"""
import random
import asyncio
from typing import Generator
"""
These are random, asyncio and typing module
"""


async def async_generator() -> Generator[float, None, None]:
    """
    This is our generator func
    """
    i: int
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
