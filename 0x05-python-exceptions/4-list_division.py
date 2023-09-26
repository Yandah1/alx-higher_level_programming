#!/usr/bin/python3

"""function that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        x = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(x)
        except TypeError:
            print("wrong type")
            result.append(x)
        except IndexError:
            print("out of range")
            result.append(x)
        finally:
            pass
    return result
