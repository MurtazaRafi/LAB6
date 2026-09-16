# Part A - List comprehensions
# 1.

numbers = range(1,21)
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

# print(squares)

# list comp
squares = [number ** 2 for number in numbers]
print(squares)
# 2.
nums = range(1, 101)
even_numbers = [num for num in nums if num % 2 == 0]
print(even_numbers)
# 3.
names = ["adam larsson", "kalle karlsson", "eva engman"]
title_cased = [name.title() for name in names]
print(title_cased)
# # 4.
# scores = [100, 80, 70, 60]
# passed = [score for score in scores if score >=70]
# print(passed)
# 5.

scores = [100, 80, 70, 60]
passed = ["Pass" if score >=70 else "Fail" for score in scores]
print(passed)

# 6. Från lesson 3 5.
words = ["This", "is", "Python"]
count = 0
for word in words:
    if len(word) >= 5:
        count += 1
print(count)
# From lesson 4 3. 
def get_long_words(words, minimum_length):
    # long_words = []
    # for word in words:
    #     if len(word) >= minimum_length:
    #         long_words.append(word)

    long_words = [word for word in words if len(word) >= minimum_length]
    return long_words

print(get_long_words(["Hej", "Hallå"], 4))



# with list comp.
long_words = [word for word in words if len(word) >= 5]
print(len(long_words))


# Part B - Dictionary and set comprehensions
# 1. 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = {num: num ** 2 for num in nums}
print(squares)

# 2.

words = ["Life", "is", "Beautiful"]
word_lengths = {word : len(word) for word in words}
print(word_lengths) 

# 
# 3.
lst = ["Python", "C#", "Java", "Java", "Python"]
lower = {element.lower() for element in lst}
print(lower)

# 4.
products = [{"product" : "car", "price" : 100000}, {"product" : "bicycle", "price" : 5000}, {"product" : "motorcycle", "price" : 20000}]

cheep_products = {element["product"] : element["price"] for element in products if element["price"] <= 20000}

print(cheep_products)

# 5.
students = [{"name": "Olle", "score": 70}, {"name": "Volkan", "score": 60}, {"name": "Karl", "score": 85}]

passed = {student["name"] : "PASS" if student["score"] >= 70 else "FAIL" for student in students}

print(passed)

# part C - enumerate

# 1. 

playlist = ["Hej hej", "Vad är det här?", "Bästa"]

for index, song in enumerate(playlist, start = 1):
    print(index, song)

# 2. 

tasks = ["Laundry", "Study", "Eat", "Walk"]

for i, task in enumerate(tasks, start=1):
    print(f"Task {i}: {task}") 

# 3. 
for i, task in enumerate(tasks, start=1):
    if i >= 2:
        print(f"Task {i}: {task}") 

# 4. Cleaner because you get the index and the value directly

for i in range(len(tasks)):
    print(i, tasks[i])

# See above for better solution

# part D - zip and unpacking
# 1.
names = ["Anna", "Karl", "Murtaza"]
scores = [80, 60, 70]

students = zip(names, scores)

for student in students:
    print(student)

# 2.
print(dict(students))

# 3.
product_names =["bicycle", "motorbike", "car"]
prices = [5000, 20000, 100000]
stock = [100, 50, 20]

items = zip(product_names, prices, stock)
for item in items:
    print(item)
# 4.

users = zip(["name 1", "name 2", "name 3"], [100, 80])
for user in users:
    print(user)

# 5.
names = ["Anna", "Karl", "Murtaza"]
scores = [80, 60, 70]

student_dictionary = {}
for key, val in zip(*[names, scores]):
    student_dictionary[key] = val

print(student_dictionary)

# 6.
x = 2
y = 3
x, y = y, x

# part E - sorted and lambda
# 1.
words =["Hej", "Jag", "Heter", "Murtaza"]

print(sorted(words, key=len))

# 2.
students = [{"name": "Olle", "score": 70}, {"name": "Volkan", "score": 60}, {"name": "Karl", "score": 85}]
ascending = sorted(students, key = lambda student: student["score"])
descending = sorted(students, key = lambda student: student["score"], reverse=True)
print(ascending)
print(descending)

# 3. 
products = [{"product" : "car", "price" : 100000}, {"product" : "bicycle", "price" : 5000}, {"product" : "motorcycle", "price" : 20000}]


sorted = sorted(products, key = lambda product: product["price"])
print(sorted) 

# 4.

# 5. 


# part F

# part G
# 1.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [new_list for sublist in matrix]