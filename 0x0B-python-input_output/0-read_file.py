#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
