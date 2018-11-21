import asyncio


async def do_some_work(x):
    print(x)


coroutine = do_some_work("hello")

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(coroutine)
finally:
    loop.close()
