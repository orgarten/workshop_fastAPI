from pydantic import BaseModel, Field

class Person(BaseModel):
    first_name: str = Field(max_length=100)
    last_name: str = Field(max_length=100)
    age: int = Field(gt=0, lt=120)

person = Person(
    first_name="Orell",
    last_name="Smith",
    age=30
)

class Book(BaseModel):
    name: str
    author: Person
    amount_in_stock: int

book = Book(
    name="FastAPI",
    author=Person(
        first_name="Bill",
        last_name="Lubanovic",
        age=50
    ),
    amount_in_stock=100
)

print(book)
