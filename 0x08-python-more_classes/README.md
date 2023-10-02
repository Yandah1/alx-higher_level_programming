This README provides an overview of the requirements and specifications for a Python class called `Rectangle`. The class is designed to define rectangles and perform various operations on them.

## Class: Rectangle

### 0. Simple rectangle
- Create an empty class `Rectangle` that defines a rectangle.

### 1. Real definition of a rectangle
- Define a `Rectangle` class with private instance attributes `width` and `height`.
- Implement properties `width` and `height` to retrieve and set the width and height of the rectangle.
- Handle data validation:
  - Width and height must be integers.
  - Width and height must be greater than or equal to 0.
  - Raise appropriate exceptions for invalid data.

### 2. Area and Perimeter
- Build upon the previous class.
- Implement public instance methods:
  - `area(self)` returns the rectangle area.
  - `perimeter(self)` returns the rectangle perimeter.
- If width or height is 0, the perimeter is 0.

### 3. String representation
- Enhance the class to provide a string representation of the rectangle.
- Implement `print()` and `str()` methods to print the rectangle with `#` characters.
- Return an empty string if width or height is 0.

### 4. Eval is magic
- Improve the class to support evaluation using `eval()`.
- Implement `repr()` to return a string representation that can recreate a new instance.
- Include a message "Bye rectangle..." when an instance is deleted.

### 5. Detect instance deletion
- Extend the class to detect instance deletions.
- Print the message "Bye rectangle..." when an instance is deleted.

### 6. How many instances
- Keep track of the number of instances created.
- Implement a class attribute `number_of_instances`.
- Increment it during each new instance instantiation and decrement it during instance deletion.

### 7. Change representation
- Modify the class to allow customization of the character used for string representation.
- Add a public class attribute `print_symbol` to specify the character used.
- Update `print()` and `str()` methods accordingly.

### 8. Compare rectangles
- Introduce a static method `bigger_or_equal(rect_1, rect_2)` that compares two rectangles based on their areas.
- Raise exceptions if the arguments are not instances of `Rectangle`.
- Return `rect_1` if both rectangles have the same area value.

### 9. A square is a rectangle
- Implement a class method `square(cls, size=0)` that returns a new `Rectangle` instance with equal width and height (i.e., a square).

Each section represents a different version or feature of the `Rectangle` class, building upon the previous one. Users can choose the appropriate version of the class based on their needs and requirements.
