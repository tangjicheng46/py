import time
import asyncio
import sys


async def say_after(delay, sentence):
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')}", sentence)


async def main():
    print(f"{time.strftime('%X')} main start...")

    await say_after(1, "Hello, ")
    await say_after(2, "world!")

    print(f"{time.strftime('%X')} main end...")


async def main2():
    print(f"{time.strftime('%X')} main start...")

    t1 = asyncio.create_task(say_after(1, "Hello, "))
    t2 = asyncio.create_task(say_after(2, "world!"))

    await asyncio.wait([t1, t2])

    print(f"{time.strftime('%X')} main end...")

if __name__ == "__main__":
    if int(sys.argv[1]) == 1:
        asyncio.run(main())
    if int(sys.argv[1]) == 2:
        asyncio.run(main2())
