#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end='')
