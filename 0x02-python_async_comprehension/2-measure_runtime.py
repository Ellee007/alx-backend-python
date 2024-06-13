#!/usr/bin/env python3
"""
This is our module
"""
import asyncio
import time
"""
These are time and asyncio modules
"""
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    This is our measure_runtime function
    """
    s: int = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.perf_counter() - s
