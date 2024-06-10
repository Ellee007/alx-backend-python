#!/usr/bin/env python3
"""
This is our python3 module
"""
import time
import asyncio
"""
These are time and asyncio module
"""
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This is our function
    """
    s: str = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
