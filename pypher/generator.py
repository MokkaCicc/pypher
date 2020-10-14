#!/usr/bin/env python

from abc import ABC, abstractclassmethod
from functools import reduce

from pypher import utils


class Generator(ABC):
    @abstractclassmethod
    def __init__(cls):
        pass


    @classmethod
    def alpha_keys(cls, length: int, debug=False) -> list:
        keys = list()
        key = list("A" * length)
        max_keys = 26**length

        keys.append(reduce((lambda a, b: a + b), key))
        while any(list(map((lambda x: False if x == 'Z' else True), key))):
            for letter_index in range(len(key)):
                if key[letter_index] == "Z":
                    key[letter_index] = "A"
                else:
                    next_alpha = chr(ord(key[letter_index]) + 1)
                    key[letter_index] = next_alpha
                    break
            keys.append(reduce((lambda a, b: a + b), key))

            if debug:
                print(f"{len(keys)}/{max_keys} keys generated")

        return keys
