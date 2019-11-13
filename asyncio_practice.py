import asyncio

async def add(start, end, wait):
    sum = 0

    for n in range(start,end):
        sum += n
    await asyncio.sleep(wait)
    print(f'Sum from {start} to {end} is {sum}')

async def main():
    task1 = loop.create_task(add(5,50000,3))
    task2 = loop.create_task(add(2,30000,2))
    task3 = loop.create_task(add(10,1000,1))
    await asyncio.wait([task1,task2,task3])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
