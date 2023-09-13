#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = [x for x in my_list if my_list.count(x) == 1]

    return sum(set(unique_list))
