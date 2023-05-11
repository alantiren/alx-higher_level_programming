#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    res = 0
    for i in range(len(sys.argv) - 1):
        res += int(sys.argv[i + 1])
    print("{}".format(res))

