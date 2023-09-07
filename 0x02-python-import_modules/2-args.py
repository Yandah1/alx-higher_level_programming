#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("0 arguments.")
    else:
        print("1 arguments:")

        for i in range(len(arguments)):
            arg = arguments[i]
            print("{}: {}".format(i + 1, arg))
