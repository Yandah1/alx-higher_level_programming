#!/usr/bin/python3
def to_subtract(list_num):
    max_value = max(list_num)
    sum_values = sum(list_num) - max_value
    return max_value - sum_values


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_value = 0
    list_num = [0]

    for ch in roman_string:
        if ch in rom_n:
            current_value = rom_n[ch]
            if current_value <= last_value:
                num += to_subtract(list_num)
                list_num = [current_value]
            else:
                list_num.append(current_value)

            last_value = current_value

    num += to_subtract(list_num)
    return num
