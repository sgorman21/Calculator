import numpy as np
import matplotlib.pyplot as plt
import re


def remove_ands(list_of_stuff):
    ands = True
    while ands:
        if "and" in list_of_stuff:
            del (list_of_stuff[list_of_stuff.index("and")])
        else:
            ands = False
    return list_of_stuff


def take_and_prep(raw_string):
    raw_string = remove_ands(raw_string.split())
    return raw_string


def find_operator_num(list_of_strings):
    list_to_operate = []
    for iterator in range(0,len(list_of_strings)):
        if not list_of_strings[iterator].isdigit():
            operator = list_of_strings[iterator]
        else:
            list_to_operate.append(int(list_of_strings[iterator]))
    return operator, list_to_operate


adding = ["add", "plus", "+"]
subtracting = ["subtract", "minus", "-", "take"]
multiplying = ["times", "multiply", "x", "*"]

def find_answer(components):
    op = components[0]
    numbers = components[1]
    if op in adding:
        result = sum(numbers)
    if op in subtracting:
        last_lot = numbers[1:len(numbers)]
        result =  numbers[0]-sum(last_lot)
    if op in multiplying:
        result = 1
        for elem in range(0,len(numbers)):
            result = result*numbers[elem]
    return result


print("Hello, I am your calculator. How can I help you today? Type quit at any time to stop.")

finished = False
while not finished:

    userwants = input()
    if userwants == "no":
        break
    problem = take_and_prep(userwants)
    components = find_operator_num(problem)
    answer = find_answer(components)
    print("Here's your answer:", answer,"\n","Would you like me to do anything else?")

    if finished:
        break