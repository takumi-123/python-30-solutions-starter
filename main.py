numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#2
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
even_numbsers = list(filter(lambda x: x % 2 == 0, numbers2))
print(even_numbsers)