#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    if a < b:
        add, sub = __import__('magic_calculation_102').add, __import__('magic_calculation_102').sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))
