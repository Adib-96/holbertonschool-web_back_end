#!/usr/bin/env python3

import random
import asyncio
"""
An asynchronous coroutine that waits for a random delay
between 0 and max_delay seconds.
Parameters:
    - max_delay (float): The maximum
    duration to wait for (default is 10 seconds).
Returns:
- float: The actual duration waited,
a random value between 0 and max_delay (inclusive).
"""


async def wait_random(max_delay: int = 10) -> float:
    """function handle coroutine"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
