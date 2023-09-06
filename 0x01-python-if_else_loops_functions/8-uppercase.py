#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(97) <= ord(c) <= ord(122):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()
