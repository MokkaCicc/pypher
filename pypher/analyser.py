#!/usr/bin/env python

from abc import ABC, abstractclassmethod
from functools import reduce

from pypher import utils
from pypher import Converter


class Analyser(ABC):
    OCURS_FR = "EAISNRTOLUDCMPGBVHFQYXJKWZ"


    @abstractclassmethod
    def __init__(cls):
        pass


    @classmethod
    def ocurs_chars(cls, message: str, percent=False, reverse=False) -> dict:
        chars = dict()
        for letter in utils.UPPER_ALPHA:
            chars[letter] = 0
        message = Converter.normalize(message)

        for char in message:
            chars[char] += 1

        # It's beautiful (sort dict by value)
        chars = {key: value for key, value in sorted(chars.items(), key=(lambda item: item[1]), reverse=not reverse)}

        if percent:
            len_msg = len(message)
            chars = {key: value*len_msg/100 for key, value in chars.items()}

        return chars


    # TODO: implemente methods
    @classmethod
    def ocurs_bigrammes(cls, message: str) -> dict:
        pass


    @classmethod
    def ocurs_trigrammes(cls, message: str) -> dict:
        pass


    @classmethod
    def ocurs_words(cls, message: str) -> dict:
        pass


    @classmethod
    def ocurs_words_length(cls, message: str) -> dict:
        pass


    @classmethod
    def coincidence_index(cls, message: str) -> float:
        ocurs_alpha = cls.ocurs_chars(message)
        len_message = reduce((lambda a, b: a + b), ocurs_alpha.values())

        coincidence = 0
        if len_message != 0:
            for value in ocurs_alpha.values():
                coincidence += value * (value - 1)

            coincidence /= len_message * (len_message - 1)

        return coincidence


    @classmethod
    def cycle_chars(cls, message: str, step: int, begin=0) -> list:
        len_message = len(message)
        letters = list()

        for letter_index in range(begin, len_message, step):
            letters.append(message[letter_index])

        return letters


    @classmethod
    def frequency_match_score(cls, message: str) -> int:
        ocurs = list(cls.ocurs_chars(message))
        most_ocurs = ocurs[0:6]
        least_ocurs = ocurs[20:26]
        most_ocurs_fr = list(cls.OCURS_FR[0:6])
        least_ocurs_fr = list(cls.OCURS_FR[20:26])

        score = 0
        for ocur in most_ocurs:
            if ocur in most_ocurs_fr:
                score += 1

        for ocur in least_ocurs:
            if ocur in least_ocurs_fr:
                score += 1

        return score


    @classmethod
    def has_lower_alpha(cls, message: str) -> bool:
        for letter in utils.LOWER_ALPHA:
            if letter in message:
                return True
        return False


    @classmethod
    def has_upper_alpha(cls, message: str) -> bool:
        for letter in utils.UPPER_ALPHA:
            if letter in message:
                return True
        return False


    @classmethod
    def has_alpha(cls, message: str) -> bool:
        for char in utils.ALPHA:
            if char in message:
                return True
        return False


    @classmethod
    def has_accents(cls, message: str) -> bool:
        for accent in utils.ACCENTS:
            if accent in message:
                return True
        return False


    @classmethod
    def has_nums(cls, message: str) -> bool:
        for num in utils.NUMS:
            if num in message:
                return True
        return False


    @classmethod
    def has_puncts(cls, message: str) -> bool:
        for punct in utils.PUNCTS:
            if punct in message:
                return True
        return False


    @classmethod
    def has_quotes(cls, message: str) -> bool:
        for quote in utils.QUOTES:
            if quote in message:
                return True
        return False


    @classmethod
    def has_brackets(cls, message: str) -> bool:
        for bracket in utils.BRACKETS:
            if bracket in message:
                return True
        return False


    @classmethod
    def keep_brackets(cls, message: str) -> str:
        for char in message:
            if char not in utils.BRACKETS:
                message = message.replace(char, "")
        return message