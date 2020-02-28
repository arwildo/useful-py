#!/bin/python3


def charCounter(inputStr):
    inputStr = inputStr.lower()
    dict = {}

    for char in inputStr:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


print("Input : ")
userStr = input(str())
print(charCounter(userStr))

# Output: {'t': 2, 'e': 1, 's': 1}
