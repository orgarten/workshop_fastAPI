from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

from pydantic_settings import BaseSettings

app = FastAPI()

class AppSettings(BaseSettings):
    version: str

settings = AppSettings(version="0.5.0")

@app.get("/version")
async def get_version():
    return settings.version

class Address(BaseModel):
    street: str
    street_number: str
    city: str
    state: str | None = None
    zip: str


class Person(BaseModel):
    id: int | None = Field(None, gt=0)
    first_name: str = Field(min_length=50)
    last_name: str = Field(min_length=50)
    address: Address | None = None


person_db: dict[int, Person] = {}

@app.post("/person")
def add_person(person: Person):
    new_id = len(person_db) + 1
    person.id = new_id
    person_db[new_id] = person
    return person

@app.get("/person")
def get_persons(id: int | None = None):
    if id is None:
        return person_db

    return person_db.get(id)

@app.get("/person")
def get_person(id: int):
    return person_db.get(id)


from fastapi import status, Response
@app.get("/hello/{name}", status_code=status.HTTP_200_OK)
def hello(name: str, response: Response):
    if name != "alice":
        return {"message": f"Hello, {name}"}

    response.status_code = status.HTTP_400_BAD_REQUEST
    return {}
