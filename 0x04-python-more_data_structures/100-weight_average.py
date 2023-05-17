#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_product = 0
    sum_weights = 0

    for tup in my_list:
        sum_product += tup[0] * tup[1]
        sum_weights += tup[1]

    return (sum_product / sum_weights)
