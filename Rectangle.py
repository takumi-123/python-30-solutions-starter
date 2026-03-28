class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
Rectangle1 = Rectangle(3, 4)

result = Rectangle1.area()
print(f"辺の長さが{Rectangle1.width}と{Rectangle1.height}の四角の面積は{result}です")