#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    #this is a dictionary of the operator as the key and function as the value
    operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }
    #checks if the operator isn't in the list of current operators
    if argv[2] not in list(operators.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    i = int(argv[1])
    j = int(argv[3])
    print("{} {} {} = {}".format(i, argv[2], j, operators[argv[2]](i, j)))
