#!/usr/bin/env python3
"""
This is our module
"""
import asyncio
from typing import List
"""
These are asyncio and typing modules
"""
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    This an async func that returns comprehension from generator
    """
    return [i async for i in async_generator()]
