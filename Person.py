class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"私の名前は{self.name}です")

    def introduce(self):
        print(f"わたしの年齢は{self.age}です")

Person1 = Person("次郎", 20)
Person1.say_hello()
Person1.introduce()