from Animal import Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")
    
    def purr(self):
        print(f"{self.name} purrs")

my_cat = Cat("Whiskers")
my_cat.speak()
my_cat.purr()