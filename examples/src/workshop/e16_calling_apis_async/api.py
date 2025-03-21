import time
import asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from starlette import status
import random
app = FastAPI()

@app.get("/test", status_code=status.HTTP_200_OK)
async def root(id: int):
    print(f"Hello from /test?id={id}")
    #time.sleep(0.1)
    await asyncio.sleep(0.1)
    if random.randint(0, 1000) > 995:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)

    return {"id": id}

if __name__ == "__main__":
    random.seed(time.time())
    uvicorn.run(app, host="0.0.0.0", port=8000)