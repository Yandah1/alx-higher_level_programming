0x04. Python - More Data Structures: Set, Dictionary
Python

# Python Functions README

This repository contains Python functions for various tasks, each designed to perform a specific operation. Below is an overview of each function and its usage.

## Table of Contents

- [Functions](#functions)
  - [square_matrix_simple](#square_matrix_simple)
  - [search_replace](#search_replace)
  - [uniq_add](#uniq_add)
  - [common_elements](#common_elements)
  - [only_diff_elements](#only_diff_elements)
  - [number_keys](#number_keys)
  - [print_sorted_dictionary](#print_sorted_dictionary)
  - [update_dictionary](#update_dictionary)
  - [simple_delete](#simple_delete)
  - [multiply_by_2](#multiply_by_2)
  - [best_score](#best_score)
  - [multiply_list_map](#multiply_list_map)
  - [roman_to_int](#roman_to_int)

## Functions

### `square_matrix_simple(matrix)`

This function computes the square value of all integers in a matrix. It takes a 2-dimensional array `matrix` as input and returns a new matrix with squared values.

### `search_replace(my_list, search, replace)`

This function replaces all occurrences of an element in a list with another element and returns a new list. It takes the initial list `my_list`, the element to replace `search`, and the new element `replace` as inputs.

### `uniq_add(my_list)`

This function adds all unique integers in a list, ensuring that each integer is only added once. It takes a list `my_list` as input and returns the sum of unique integers.

### `common_elements(set_1, set_2)`

This function returns a set of common elements present in two sets `set_1` and `set_2`.

### `only_diff_elements(set_1, set_2)`

This function returns a set of all elements present in only one of the two sets `set_1` and `set_2`.

### `number_keys(a_dictionary)`

This function returns the number of keys in a dictionary `a_dictionary`.

### `print_sorted_dictionary(a_dictionary)`

This function prints a dictionary with keys sorted in alphabetical order. It assumes that all keys are strings and that values can be of any type.

### `update_dictionary(a_dictionary, key, value)`

This function replaces or adds a key-value pair in a dictionary `a_dictionary`. If the key exists, the value is replaced; if not, a new key-value pair is added.

### `simple_delete(a_dictionary, key="")`

This function deletes a key in a dictionary `a_dictionary` if it exists. The key to delete is provided as the `key` parameter.

### `multiply_by_2(a_dictionary)`

This function returns a new dictionary with all values multiplied by 2. It assumes that all values in the dictionary are integers.

### `best_score(a_dictionary)`

This function returns the key with the biggest integer value in a dictionary. If no score is found, it returns `None`.

### `multiply_list_map(my_list, number=0)`

This function returns a new list with all values multiplied by a specified number using the `map` function. It preserves the length of the original list and does not modify it.

### `roman_to_int(roman_string)`

This function converts a Roman numeral to an integer. It takes a Roman numeral string `roman_string` as input and returns an integer between 1 and 3999. If the input is not a valid string or `None`, it returns 0.
