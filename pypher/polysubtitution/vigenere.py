#!/usr/bin/env python

from abc import ABC, abstractclassmethod
from functools import reduce

from pypher import utils
from pypher import Converter
from pypher import Analyser


class Vigenere(ABC):
    @abstractclassmethod
    def __init__(cls):
        pass


    @classmethod
    def encrypt(cls, message: str, key: str) -> str:
        message = Converter.normalize(message)

        # duplicate the key to the length of the message
        key = key.upper() * ((len(message) // len(key) + 1))
        key = key[:len(message)]

        message_indexes = Converter.alpha_to_indexes(message)
        key_indexes = Converter.alpha_to_indexes(key)

        crypted_message_indexes = list()

        for i in range(len(message_indexes)):
            crypted_message_indexes.append(message_indexes[i] + key_indexes[i])

        crypted_message = Converter.indexes_to_alpha(crypted_message_indexes)
        return crypted_message


    @classmethod
    def decrypt(cls, crypted_message: str, key: str) -> str:
        crypted_message = Converter.normalize(crypted_message)

        # duplicate the key to the length of the message
        key = key.upper() * ((len(crypted_message) // len(key) + 1))
        key = key[:len(crypted_message)]

        crypted_message_indexes = Converter.alpha_to_indexes(crypted_message)
        key_indexes = Converter.alpha_to_indexes(key)

        message_indexes = list()

        for i in range(len(crypted_message_indexes)):
            if crypted_message_indexes[i] < key_indexes[i]:
                crypted_message_indexes[i] += 26
            message_indexes.append(abs(crypted_message_indexes[i] - key_indexes[i]))

        message = Converter.indexes_to_alpha(message_indexes)
        return message


    # TODO: yes.
    @classmethod
    def estimate_key_length(cls, crypted_message: str) -> dict:
        pass


    @classmethod
    def estimate_key_chars(cls, crypted_message: str, key_length: int) -> dict:
        crypted_message = Converter.normalize(crypted_message)
        key_chars = dict()

        for i in range(key_length):
            crypted_chunk = reduce((lambda a, b: a + b), Analyser.cycle_chars(crypted_message, key_length, begin=i))
            chars = dict()

            for letter in utils.UPPER_ALPHA:
                chunk = Vigenere.decrypt(crypted_chunk, letter)
                score = Analyser.frequency_match_score(chunk)
                chars[letter] = score

                chars = {key: value for key, value in sorted(chars.items(), key=(lambda item: item[1]), reverse=True)}

            key_chars[i] = chars

        return key_chars