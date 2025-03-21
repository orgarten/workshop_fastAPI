import httpx
import asyncio

async def async_range(start, stop):
    for i in range(start, stop):
        yield i
        await asyncio.sleep(0.0)

async def call_test_endpoint_simple(tries: int):
    async with httpx.AsyncClient() as client:
        async for i in async_range(0, tries):
            response = await client.get(f"http://localhost:8000/test?id={i}")

            if response.status_code != 200:
                print(f"Error for id {i}: {response.status_code} - {response.text}")

        print("Done")

async def call_test_endpoint_simple_2(tries: int):
    async with httpx.AsyncClient() as client:
        futures = []
        for i in range(0, tries):
            futures.append(client.get(f"http://localhost:8000/test?id={i}"))

        for f in futures:
            response = await f
            if response.status_code != 200:
                print(f"Error for id {i}: {response.status_code} - {response.text}")

        print("Done")

if __name__ == "__main__":
    asyncio.run(call_test_endpoint_simple_2(1000))