#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        divisible_by_2 = i % 2 == 0
        new_list.append(divisible_by_2)
    return new_list
