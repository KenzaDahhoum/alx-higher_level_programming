#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    res = 0
    if i == 0:
        print("0")
    else:
        for arg in sys.argv:
            if arg != sys.argv[0]:
                res += int(arg)
        print("{}".format(res))
