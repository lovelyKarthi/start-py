"""Asyncio pattern with aiohttp (illustrative)"""
import asyncio

async def fake_fetch(i):
    await asyncio.sleep(0.05)
    return f'result-{i}'

async def main():
    tasks = [fake_fetch(i) for i in range(20)]
    res = await asyncio.gather(*tasks)
    print('len', len(res))

if __name__ == '__main__':
    asyncio.run(main())
