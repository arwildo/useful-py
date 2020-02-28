#!/bin/python3
import random
from random import randrange
import string

alphabet = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)
numbers = list(string.digits)
alphabet += alphabet_lower
alphabet += numbers


def wordLister(size=randrange(4, 8), chars=(alphabet)):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    id = wordLister()
    print(id)
