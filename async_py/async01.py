import asyncio


async def f1():
    print(1)
    await asyncio.sleep(1)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(1)
    print(4)

task_list = [
    f1(),
    f2()
]

asyncio.run(asyncio.wait(task_list))
