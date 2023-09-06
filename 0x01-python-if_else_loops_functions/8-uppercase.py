#!/usr/bin/python3
def uppercase(str):
    rusult = ""
    for c in str:
        if ord(97) <= ord(c) <= ord(122):
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
