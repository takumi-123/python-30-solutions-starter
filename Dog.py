from Animal import Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

mydog = Dog("Buddy")
mydog.speak()