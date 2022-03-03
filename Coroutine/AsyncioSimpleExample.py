import asyncio
import time

# https://www.maxlist.xyz/2020/03/29/python-coroutine/
# 1. 一個簡單的範例

now = lambda: time.time()


async def dosomething(num):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(2)
    print('第 {} 任務，第二步'.format(num))


async def dosomethingNum(num, time):
    print('第 {} 任務，第一步'.format(num))
    await asyncio.sleep(time)
    print('第 {} 任務，第二步'.format(num))

    #
    # 第 3 任務，第一步
    # 第 2 任務，第一步
    # 第 1 任務，第一步
    # 第 3 任務，第二步
    # 第 1 任務，第二步
    # 第 2 任務，第二步
    # TIME:  10.007741689682007

if __name__ == "__main__":
    start = now()
    # tasks = [dosomething(i) for i in range(5)]
    tasks2 = [dosomethingNum(1, 3), dosomethingNum(2, 10), dosomethingNum(3, 1)]
    asyncio.run(asyncio.wait(tasks2))
    print('TIME: ', now() - start)

