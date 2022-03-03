import asyncio
import time

# https://www.maxlist.xyz/2020/03/29/python-coroutine/
# 4. 如何建立任務 Task？

async def dosomething(num):
    print('start{}'.format(num))
    await asyncio.sleep(num)
    print('sleep{}'.format(num))

async def main():
    task1 = asyncio.create_task(dosomething(1))
    task2 = asyncio.create_task(dosomething(2))
    task3 = asyncio.create_task(dosomething(3))
    await task1
    await task2
    await task3
    #
    # start1
    # start2
    # start3
    # sleep1
    # sleep2
    # sleep3
    # 3.0026755332946777

async def main2():
    await asyncio.create_task(dosomething(1))
    await asyncio.create_task(dosomething(2))
    await asyncio.create_task(dosomething(3))
    # start1
    # sleep1
    # start2
    # sleep2
    # start3
    # sleep3
    # 失去 await 用意 6.007076740264893

if __name__ == '__main__':
    time_start = time.time()
    # 如何建立任務 Task？
    # main() function 里面 asyncio.create_task
    asyncio.run(main())
    print(time.time() - time_start)