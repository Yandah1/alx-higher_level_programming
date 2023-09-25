
Python Exception Handling Functions

This repository contains a collection of Python functions that demonstrate how to handle exceptions without using any external modules. These functions are designed to perform various tasks while gracefully handling potential errors.

## `safe_print_list(my_list=[], x=0)`

This function prints the first `x` elements of a list (`my_list`) on the same line followed by a new line. It can handle lists containing any type of data (integers, strings, etc.). If `x` is greater than the length of `my_list`, it will still print as many elements as possible and return the real number of elements printed. This function uses `try` and `except` for error handling and does not rely on importing any modules or using the `len()` function.

## `safe_print_integer(value)`

This function prints an integer (if `value` is an integer) using the `"{:d}".format()` method. It returns `True` if the integer has been correctly printed; otherwise, it returns `False`. This function is designed to handle different data types as input and uses `try` and `except` for error handling. Importing modules or using `type()` is not allowed.

## `safe_print_list_integers(my_list=[], x=0)`

This function prints the first `x` integers from a list (`my_list`) on the same line followed by a new line. It skips non-integer values in the list and can handle cases where `x` is greater than the length of `my_list`. If an exception occurs due to insufficient elements in the list, it is expected. This function uses `try` and `except` for error handling and the `"{:d}".format()` method for printing integers. Importing modules or using `len()` is prohibited.

## `safe_print_division(a, b)`

This function divides two integers, `a` and `b`, and prints the result as "Inside result: {result}". It returns the value of the division or `None` if an exception occurs during division by zero. This function uses `try`, `except`, and `finally` for error handling and the `"{}".format()` method to format the result. It does not rely on importing any modules.

## `list_division(my_list_1, my_list_2, list_length)`

This function divides corresponding elements from two lists, `my_list_1` and `my_list_2`, and returns a new list of length `list_length` with the division results. If two elements can't be divided, the result is set to 0. If an element is not an integer or float, it prints "wrong type." If the division by zero occurs, it prints "division by 0." If either `my_list_1` or `my_list_2` is too short, it prints "out of range." This function uses `try`, `except`, and `finally` for error handling and does not rely on importing any modules.

## `raise_exception()`

This function raises a type exception and does not require importing any modules.

## `raise_exception_msg(message="")`

This function raises a name exception with an optional custom `message` and does not require importing any modules.


