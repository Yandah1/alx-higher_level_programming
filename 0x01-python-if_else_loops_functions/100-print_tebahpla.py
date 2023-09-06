#!/usr/bin/python3

def print_reverse_alphabet():
    for c in range(ord('Z'), ord('A') - 1, -1):
        print("{}".format(chr(c)), end="")
        if c != ord('A'):
            print("{}".format(chr(c + 32)), end="")
    print()
