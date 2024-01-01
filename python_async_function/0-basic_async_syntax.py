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


async def wait_random(max_delay=10):
    """function handle coroutine"""
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)
