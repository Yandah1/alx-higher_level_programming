0x06-python-classes


README.md

Python - Classes and Objects
In this project, I began practicing object-oriented programming using classes and objects in Python. I learned about attributes, methods, and properties as well as data abstraction, data encapsulation, and information hiding.

0. My first square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write an empty class Square that defines a square:

You are not allowed to import any module

1. Square with size
mandatory

Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
Why?

Why size is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

2. Size validation
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

3. Area of a square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 2-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module

4. Access and update private attribute
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
You are not allowed to import any module

5. Printing a square
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
You are not allowed to import any module
