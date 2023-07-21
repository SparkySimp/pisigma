#!/usr/bin/python3
# pisigma.py - Implements pi/sigma

if __name__ == '__main__':
    # simple cli driver
    from sys import argv, exit
    from pisigma import pisigma, I
    if len(argv) != 3:
        exit(31)
    else:
        n = int(argv[1])
        x = int(argv[2])
        print(f"pisigma({n}, {x}, I) = {pisigma(n, x, I)}")
