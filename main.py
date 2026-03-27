original_numbers = [1, 2, 3, 4, 5]
doubled_numbers = [number * 2 for number in original_numbers]
print(doubled_numbers)

mixed_numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [numbers2 for numbers2 in mixed_numbers if numbers2 % 2 == 0]
print(even_numbers)

fruits_names = ["apple", "banana", "cherry"]
fruits_numbers = [len(name) for name in fruits_names]
print(fruits_numbers)

lowercase_names = ["alice", "bob", "charlie"]
upper_names = [names.upper() for names in lowercase_names]
print(upper_names)

spuares = [i ** 2 for i in range(10)]
print(spuares)

scores = [5, 12, 8, 20]
check_scores = ["OK" if score >= 10 else "NG" for score in scores]
print(check_scores)
