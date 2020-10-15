#!/usr/bin/env python

from abc import ABC, abstractmethod
from random import random

from pypher import utils


class Converter(ABC):
    """Tool to easily transform and manipulate strings.
    This class is abstract and cannot be instanciate, all methods are class methods.
    """
    @classmethod
    @abstractmethod
    def __init__(cls):
        pass

    @classmethod
    def alpha_to_indexes(cls, message: str) -> list[int]:
        """Convert a message into a list of position in the alphabet.
        This method normalize the message before the processing.

        Args:
            message (str): the message to process.

        Returns:
            list[int]: the list of indexes.
        """
        message = cls.normalize(message)
        indexes = list()

        for letter in message:
            indexes.append(utils.UPPER_ALPHA.index(letter))

        return indexes

    @classmethod
    def indexes_to_alpha(cls, indexes: list[int]) -> str:
        """Convert a list of indexes into a message.
        If an index is too long, it will be looped.

        Args:
            indexes (list[int]): The list of indexes.

        Returns:
            str: the corresponding message.
        """
        message = ""

        for index in indexes:
            index %= len(utils.UPPER_ALPHA)
            message += utils.UPPER_ALPHA[index]

        return message

    @classmethod
    def normalize(cls, message: str) -> str:
        """Normalize the message.
        It will convert accents into ASCII, upper all alphas and removes anything else.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        message = cls.accents_to_ascii(message)
        message = message.upper()
        message = cls.keep_upper_alpha(message)

        return message

    @classmethod
    def remove_lower_alpha(cls, message: str) -> str:
        """Remove lower alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        for char in utils.LOWER_ALPHA:
            message = message.replace(char, "")
        return message

    @classmethod
    def keep_lower_alpha(cls, message: str) -> str:
        """Only keep lower alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message
        """
        for char in message:
            if char not in utils.LOWER_ALPHA:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_upper_alpha(cls, message: str) -> str:
        """Remove upper alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        for char in utils.UPPER_ALPHA:
            message = message.replace(char, "")
        return message

    @classmethod
    def keep_upper_alpha(cls, message: str) -> str:
        """Only keep upper alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        for char in message:
            if char not in utils.UPPER_ALPHA:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_alpha(cls, message: str) -> str:
        """Remove alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        for char in utils.ALPHA:
            message = message.replace(char, "")
        return message

    @classmethod
    def keep_alpha(cls, message: str) -> str:
        """Only keep alphas from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formated message.
        """
        for char in message:
            if char not in utils.ALPHA:
                message = message.replace(char, "")
        return message

    @classmethod
    def random_capitals(cls, message: str, luck: float = 0.5) -> str:
        """Randomize capitals in the message.

        Args:
            message (str): the message to format.
            luck (float, optional): the luck of a char to be uppercase. Defaults to 0.5.

        Returns:
            str: the formated message.
        """
        formatted_message = ""
        for char in message:
            if random() < luck:
                formatted_message += char.upper()
            else:
                formatted_message += char.lower()
        return formatted_message

    @classmethod
    def remove_accents(cls, message: str) -> str:
        """Remove accents from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for accent in utils.ACCENTS:
            message = message.replace(accent, "")
        return message

    @classmethod
    def keep_accents(cls, message: str) -> str:
        """Only keep accent from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.ACCENTS:
                message = message.replace(char, "")
        return message

    @classmethod
    def accents_to_ascii(cls, message: str) -> str:
        """Convert accents into ASCII in the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        return message.translate(utils.ACCENTS_TRANS)

    @classmethod
    def remove_nums(cls, message: str) -> str:
        """Remove numbers from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for num in utils.NUMS:
            message = message.replace(num, "")
        return message

    @classmethod
    def keep_nums(cls, message: str) -> str:
        """Only keep numbers from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.NUMS:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_puncts(cls, message: str) -> str:
        """Remove ponctuations from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for punct in utils.PUNCTS:
            message = message.replace(punct, "")
        return message

    @classmethod
    def keep_puncts(cls, message: str) -> str:
        """Only keep punctuations from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.PUNCTS:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_quotes(cls, message: str) -> str:
        """Remove quotes from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for quote in utils.QUOTES:
            message = message.replace(quote, "")
        return message

    @classmethod
    def keep_quotes(cls, message: str) -> str:
        """Only keep quotes from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.QUOTES:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_brackets(cls, message: str) -> str:
        """Remove brackets from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for bracket in utils.BRACKETS:
            message = message.replace(bracket, "")
        return message

    @classmethod
    def keep_brackets(cls, message: str) -> str:
        """Only keep brackets from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.BRACKETS:
                message = message.replace(char, "")
        return message

    @classmethod
    def remove_spaces(cls, message: str) -> str:
        """Remove spaces from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for space in utils.SPACES:
            message = message.replace(space, "")
        return message

    @classmethod
    def keep_spaces(cls, message: str) -> str:
        """Only keep spaces from the message.

        Args:
            message (str): the message to format.

        Returns:
            str: the formatted message.
        """
        for char in message:
            if char not in utils.SPACES:
                message = message.replace(char, "")
        return message
