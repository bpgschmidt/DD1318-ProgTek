import copy
import math
import random


# Uppgift 1 (givet)

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x


x_list = [11, 22, 33, 44]

x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))


# Uppgift 2 (math solve)

def my_function(x):
    math_solve = x ** 2 + math.sin(x)
    return math_solve


# Uppgift 3 (dice roll)

def roll_dice(n):
    dicesum = 0
    for k in (1, n + 1):
        dicesum += random.randint(1, 6)
    return dicesum


# Uppgift 4 (bubble sort)

def my_sort_list(list):
    # Go through each element in the list
    for n in range(len(list)):
        # for each element in the list in range n-1:
        for m in range(n + 1, len(list)):
            # if the element before is larger, change the numbers
            if list[n] > list[m]:
                list[n], list[m] = list[m], list[n]
    return list


# Uppgift 5 (bandit language)

def bandit_language(string):
    consonants = ["q", "w", "r", "t", "p", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    translation = ""
    for i in range(len(string)):
        if string[i] in consonants:
            translation += string[i] + "o" + string[i]
        else:
            translation += string[i]
    return translation
