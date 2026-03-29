from typing import List
name: str = "Alice"
age: int = 20
print(f"{name} is {age} years old")

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(3, 5)
print(result)

numbers: list[int]= [10, 20, 30, 40, 50]
total: int = sum(numbers)
print(f"total: {total}")