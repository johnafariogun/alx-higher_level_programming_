#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0")

    else:
        total = 0
        for i in range(argc):
            total += int(argv[i + 1])
        print(total)
