# -*- coding: utf-8 -*-
import asyncio
import time

from astartool.project import coast_time


@coast_time
def my_add(a, b):
    time.sleep(0.1)
    return a + b


@coast_time
async def my_add_2(a, b):
    await asyncio.sleep(0.1)
    return a + b


if __name__ == '__main__':
    my_add(1, 2)
    asyncio.get_event_loop().run_until_complete(my_add_2(3, 5))
