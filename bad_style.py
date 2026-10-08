import math


def calculate_area(radius):
    area = math.pi * radius**2
    return area


def greet(name):
    print("Hello, " + name + "!")


numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

result = calculate_area(5)
print("Area:", result)
greet("Developer")
