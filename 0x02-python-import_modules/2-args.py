#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    num_args = len(arguments)

    if num_args == 0:
        print("0 arguments.")
        print(".")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s")))

        for i in arg in enumerate(arguments, start = 1)):
            print("{}: {}".format(i, arg))
