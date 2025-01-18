import asyncio


async def process_data(data):
    print(f'Processing {data}')
    await asyncio.sleep(10)
    print(f'Processed {data}')
    return data * 2


async def main():
    data = [1, 2, 3, 4, 5]
    tasks = [process_data(d) for d in data]
    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
