#!/usr/bin/python3
# 100-print_tebahpla.py
for i in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i - 32), end="")
