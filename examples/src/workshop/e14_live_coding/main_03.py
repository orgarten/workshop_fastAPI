from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
import dataclasses

class Person(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    age: int = Field(gt=0, lt=120)

app = FastAPI()

@dataclasses.dataclass
class Person_Names:
    first_name: str
    last_name: str
    age: int


fake_db = {
    1: Person_Names(first_name="John", last_name="Smith", age=1)
}



@app.post("/person")
def post_person(person: Person):
    new_index = len(fake_db) + 1
    fake_db[new_index] = Person_Names(**person.model_dump())
    return fake_db

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)