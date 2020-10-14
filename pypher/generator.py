#!/usr/bin/env python

from abc import ABC, abstractmethod
from functools import reduce

from pypher import utils


class Generator(ABC):
    @classmethod
    @abstractmethod
    def __init__(cls):
        pass


    @classmethod
    def shifted_alpha(cls, shifts: int, reverse: bool = False, lower: bool = True) -> str:
        """Generate a shifted alpabet, in lower or upper case.

        Args:
            shifts (int): the number of shifts.
            reverse (bool, optionnal): the direction of the shift. Default to False.
            lower (bool, optional): if the alphabet need to be lowercase. Defaults to True.

        Returns:
            str: the shifted alphabet.
        """

        # negate shifts too long
        shifts %= len(utils.LOWER_ALPHA)
        if lower:
            alpha = utils.LOWER_ALPHA[shifts:] + utils.LOWER_ALPHA[:shifts]
        else:
            alpha = utils.UPPER_ALPHA[shifts:] + utils.UPPER_ALPHA[:shifts]

        return alpha


    # TODO: simplify method and prevent to long generation of key. (maybe separate into two methods)
    @classmethod
    def alpha_keys(cls, length: int) -> list[str]:
        """Generate all possibles keys for a certain lenght. Be careful a lenght too big can make some time to process.

        Args:
            length (int): the max lenght of the key.

        Returns:
            list[str]: the list off all possible keys.
        """

        keys = list()
        key = list("A" * length)
        max_keys = 26**length

        # HACK: This is black magic.
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

        return keys
