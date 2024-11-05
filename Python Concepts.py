# Single-line comment
'''
Multi-line
comment
'''

# Variables and Data Types
number = 10  # integer
floating_point = 3.14  # float
text = "Hello, world!"  # string
boolean = True  # boolean
none_value = None  # None

# Arithmetic Operators
addition = 5 + 3  # 8
subtraction = 10 - 4  # 6
multiplication = 2 * 5  # 10
division = 15 / 3  # 5.0
floor_division = 15 // 2  # 7
modulo = 15 % 4  # 3
exponentiation = 2 ** 3  # 8

# String Manipulation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"  # "Hello, Alice!"
length = len(message)  # 13
uppercase = message.upper()  # "HELLO, ALICE!"
lowercase = message.lower()  # "hello, alice!"
substring = message[7:12]  # "Alice"

# Control Flow Statements
if number > 5:
    print("Number is greater than 5")
elif number == 5:
    print("Number is equal to 5")
else:
    print("Number is less than 5")

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

while number > 0:
    print(number)
    number -= 1

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.insert(1, "orange")
fruits.remove("banana")
print(fruits[2])  # "cherry"
print(len(fruits))  # 3

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "London"}
print(person["name"])  # "Alice"
person["occupation"] = "Engineer"
del person["age"]
print(len(person))  # 3

# Functions
def greet(name):
    print("Hello, " + name + "!")
    
greet("Bob")  # "Hello, Bob!"

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)  # 7

# Classes and Objects
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())  # 15

# Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
