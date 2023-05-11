#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    res = 0
    for arg in args:
        res += int(arg)
    print(res)
