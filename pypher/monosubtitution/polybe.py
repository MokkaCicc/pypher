#!/usr/bin/env python

from abc import ABC, abstractclassmethod

from pypher import Converter


class Polybe(ABC):
    @abstractclassmethod
    def __init__(cls):
        pass


    @abstractclassmethod
    def encrypt(cls, message: str, key: str) -> str:
        message = Converter.accents_to_ascii(message)
        message = message.upper()

        grid = dict()
        x = 1
        y = 1
        for letter in key:
            # cords of the letter in the grid
            grid[letter] = str(x * 10 + y)
            y += 1
            # next line
            if y > 5:
                x += 1
                y = 1

        crypted_message = ""
        for letter in message:
            if letter in grid:
                crypted_message += grid[letter]
            else: 
                crypted_message += letter

        return crypted_message

