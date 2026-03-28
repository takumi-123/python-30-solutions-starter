from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int

person = Person(name="Alice", age=20)
print(person)

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prints(self):
        print(f"名前:{self.name}")
        print(f"年齢:{self.age}")

User1 = User("Bob", 35)
User1.prints()

@dataclass
class Book:
    title: str
    price: int=0

    def discount(self, rate: int) -> int:
        discount_price = self.price * (100-rate) // 100
        return discount_price

book1 = Book(title="Python入門")
book2 = Book(title="javaScript基礎", price=1300)
book3 = Book(title="AWS実践", price=1000)
print(book1)
print(book2)
result = book3.discount(20)
print(result)