#!/usr/bin/python3
# 101-stats.py

"""Reads stdin line by line and computes metrics."""


import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
total_size = 0
status_counts = {code: 0 for code in status_codes}

try:
    for i, line in enumerate(sys.stdin, 1):
        tokens = line.split()
        if len(tokens) >= 7:
            status_code = tokens[-2]
            file_size = int(tokens[-1])
            if status_code in status_codes:
                status_counts[status_code] += 1
            total_size += file_size
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                count = status_counts[code]
                if count > 0:
                    print("{}: {}".format(code, count))
            print()

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        count = status_counts[code]
        if count > 0:
            print("{}: {}".format(code, count))
