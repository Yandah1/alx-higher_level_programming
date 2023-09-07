#!/usr/bin/python3

def calculate(a, operator, b):
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in operators:
        return "Unknown operator. Available operators: +, -, * and /"
    return operators[operator](a, b)


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = calculate(a, operator, b)
    print("{} {} {} = {}".format(a, operator, b, result))
