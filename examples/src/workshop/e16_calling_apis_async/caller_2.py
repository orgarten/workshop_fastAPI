import httpx
import asyncio



async def call_test_endpoint(tries: int, chunk: int):
    async with httpx.AsyncClient() as client:
        for i in range(0, tries, chunk):
            tasks = [client.get(f"http://localhost:8000/test?id={j}") for j in range(i, i+chunk)]

            responses = await asyncio.gather(*tasks)

            for index, response in enumerate(responses):
                if response.status_code != 200:
                    print(f"Error for id {i+index}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    asyncio.run(call_test_endpoint(1000, 200))