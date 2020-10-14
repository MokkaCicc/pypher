#!/usr/bin/env python

from abc import ABC, abstractclassmethod
from random import randint

from pypher import utils


class Converter(ABC):
    @abstractclassmethod
    def __init__(cls):
        pass


    @classmethod
    def alpha_to_indexes(cls, message: str) -> list:
        message = cls.normalize(message)
        message = list(message)
        indexes = list()

        for i in range(len(message)):
            letter = message[i]
            indexes.append(utils.UPPER_ALPHA.index(letter))

        return indexes


    @classmethod
    def indexes_to_alpha(cls, indexes: list) -> str:
        message = ""

        for i in indexes:
            i = i % len(utils.UPPER_ALPHA)
            message += utils.UPPER_ALPHA[i]

        return message



    @classmethod
    def normalize(cls, message: str) -> str:
        message = cls.accents_to_ascii(message)
        message = message.upper()
        message = cls.keep_upper_alpha(message)

        return message


    @classmethod
    def remove_lower_alpha(cls, message: str) -> str:
        for letter in utils.LOWER_ALPHA:
            message = message.replace(letter, "")
        return message


    @classmethod
    def keep_lower_alpha(cls, message: str) -> str:
        for char in message:
            if char not in utils.LOWER_ALPHA:
                message = message.replace(char, "")
        return message


    @classmethod
    def remove_upper_alpha(cls, message: str) -> str:
        for letter in utils.UPPER_ALPHA:
            message = message.replace(letter, "")
        return message


    @classmethod
    def keep_upper_alpha(cls, message: str) -> str:
        for char in message:
            if char not in utils.UPPER_ALPHA:
                message = message.replace(char, "")
        return message


    @classmethod
    def remove_alpha(cls, message: str) -> str:
        for letter in utils.ALPHA:
            message = message.replace(letter, "")
        return message


    @classmethod
    def keep_alpha(cls, message: str) -> str:
        for char in message:
            if char not in utils.ALPHA:
                message = message.replace(char, "")
        return message


    @classmethod
    def random_capitals(cls, message: str, luck=50) -> str:
        formatted_message = ""
        for letter in message:
            if randint(1, 100) < luck:
                formatted_message += letter.upper()
            else:
                formatted_message += letter.lower()
        return formatted_message


    @classmethod
    def remove_accents(cls, message: str) -> str:
        for accent in utils.ACCENTS:
            message = message.replace(accent, "")
        return message


    @classmethod
    def keep_accents(cls, message: str) -> str:
        for char in message:
            if char not in utils.ACCENTS:
                message = message.replace(char, "")
        return message


    @classmethod
    def accents_to_ascii(cls, message: str) -> str:
        return message.translate(utils.ACCENTS_TRANS)


    @classmethod
    def remove_nums(cls, message: str) -> str:
        for num in utils.NUMS:
            message = message.replace(num, "")
        return message


    @classmethod
    def keep_nums(cls, message: str) -> str:
        for char in message:
            if char not in utils.NUMS:
                message = message.replace(char, "")
        return message


    @classmethod
    def remove_puncts(cls, message: str) -> str:
        for punct in utils.PUNCTS:
            message = message.replace(punct, "")
        return message


    @classmethod
    def keep_puncts(cls, message: str) -> str:
        for char in message:
            if char not in utils.PUNCTS:
                message = message.replace(char, "")
        return message


    @classmethod
    def remove_quotes(cls, message: str) -> str:
        for quote in utils.QUOTES:
            message = message.replace(quote, "")
        return message


    @classmethod
    def keep_quotes(cls, message: str) -> str:
        for char in message:
            if char not in utils.QUOTES:
                message = message.replace(char, "")
        return message


    @classmethod
    def remove_brackets(cls, message: str) -> str:
        for bracket in utils.BRACKETS:
            message = message.replace(bracket, "")
        return message


    @classmethod
    def has_spaces(cls, message: str) -> bool:
        for space in SPACES:
            if space in message:
                return True
        return False


    @classmethod
    def remove_spaces(cls, message: str) -> str:
        for space in utils.SPACES:
            message = message.replace(space, "")
        return message


    @classmethod
    def keep_spaces(cls, message: str) -> str:
        for char in message:
            if char not in utils.SPACES:
                message = message.replace(char, "")
        return message
