#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    argv = argv[1:]
    argc = len(argv)
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    i = int(argv[0])
    j = int(argv[2])
    operator = argv[1]

    if operator == '+':
        result = add(i, j)
    elif operator == '-':
        result = sub(i, j)
    elif operator == '*':
        result = mul(i, j)
    elif operator == '/':
        result = div(i, j)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(i, operator, j, result))
