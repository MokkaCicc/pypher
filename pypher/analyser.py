#!/usr/bin/env python

from abc import ABC, abstractmethod
from functools import reduce

from pypher import utils
from pypher import Converter


class Analyser(ABC):
	"""Tools to analyse some message.
	This class is abstract and cannot be instanciate, all methods are
	class methods.
	"""

	@classmethod
	@abstractmethod
	def __init__(cls):
		pass

	@classmethod
	def ocurs_chars(cls, message: str, percent: bool = False, reverse: bool = False) -> dict[str, float]:
		"""Count all ocurences of char in the message.
		This class normalize the message before process it.

		Args:
			message (str): the message to process.
			percent (bool, optional): if the ocurences need to be
				specied as percent. Defaults to False.
			reverse (bool, optional): dict sort in reverse order.
				Defaults to False.

		Returns:
			dict[str, int]: the dict of all ocurences.
		"""
		chars = dict()
		for letter in utils.UPPER_ALPHA:
			chars[letter] = 0.0
		message = Converter.normalize(message)

		for char in message:
			chars[char] += 1

		# It's beautiful (sort dict by value)
		chars = {key: value for key, value in sorted(chars.items(), key=(lambda item: item[1]), reverse=not reverse)}

		if percent:
			len_msg = len(message)
			chars = {key: value*100/len_msg for key, value in chars.items()}

		return chars

	# TODO: implemente methods and tests
	@classmethod
	def ocurs_bigrammes(cls, message: str) -> dict[str, int]:
		pass

	@classmethod
	def ocurs_trigrammes(cls, message: str) -> dict[str, int]:
		pass

	@classmethod
	def ocurs_ngrammes(cls, message: str) -> dict[str, int]:
		pass

	@classmethod
	def ocurs_words(cls, message: str) -> dict[str, int]:
		pass

	@classmethod
	def ocurs_words_length(cls, message: str) -> dict[str, int]:
		pass

	@classmethod
	def coincidence_index(cls, message: str) -> float:
		"""Calculate the coincidence index of the message.
		This is the probability of chars repetition.

		Args:
			message (str): the message to process.

		Returns:
			float: the coincidence index.
		"""
		ocurs_alpha = cls.ocurs_chars(message)
		len_message = reduce((lambda a, b: a + b), ocurs_alpha.values())

		coincidence = 0
		if len_message != 0:
			for value in ocurs_alpha.values():
				coincidence += value * (value - 1)

			coincidence /= len_message * (len_message - 1)

		return coincidence

	@classmethod
	def cycle_chars(cls, message: str, step: int, begin: int = 0) -> list[str]:
		"""Return all chars with a position multiple of step.

		Args:
			message (str): the message to process.
			step (int): the step of the cycle.
			begin (int, optional): offset for the begin. Defaults to 0.

		Returns:
			list[str]: the list of the chars.
		"""
		len_message = len(message)
		letters = list()

		for letter_index in range(begin, len_message, step):
			letters.append(message[letter_index])

		return letters

	@classmethod
	def frequency_match_score(cls, message: str) -> int:
		"""Caculate the frequency match score.
		This is the number of commons chars in the 6 firsts and lasts chars of the ocurences of a language.

		Args:
			message (str): the message to process.

		Returns:
			int: the frequency match score.
		"""
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
		"""Check if the message has alphas.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for letter in utils.LOWER_ALPHA:
			if letter in message:
				return True
		return False

	@classmethod
	def has_upper_alpha(cls, message: str) -> bool:
		"""Check if the message has alphas.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for letter in utils.UPPER_ALPHA:
			if letter in message:
				return True
		return False

	@classmethod
	def has_alpha(cls, message: str) -> bool:
		"""Check if the message has alphas.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for char in utils.ALPHA:
			if char in message:
				return True
		return False

	@classmethod
	def has_accents(cls, message: str) -> bool:
		"""Check if the message has accents.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for accent in utils.ACCENTS:
			if accent in message:
				return True
		return False

	@classmethod
	def has_nums(cls, message: str) -> bool:
		"""Check if the message has numbers.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for num in utils.NUMS:
			if num in message:
				return True
		return False

	@classmethod
	def has_puncts(cls, message: str) -> bool:
		"""Check if the message has punctuations.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for punct in utils.PUNCTS:
			if punct in message:
				return True
		return False

	@classmethod
	def has_quotes(cls, message: str) -> bool:
		"""Check if the message has quotes.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for quote in utils.QUOTES:
			if quote in message:
				return True
		return False

	@classmethod
	def has_brackets(cls, message: str) -> bool:
		"""Check if the message has brackets.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for bracket in utils.BRACKETS:
			if bracket in message:
				return True
		return False

	@classmethod
	def has_spaces(cls, message: str) -> bool:
		"""Check if the message has spaces.

		Args:
			message (str): the message to analyse.

		Returns:
			bool: if the message check the condition.
		"""
		for space in utils.SPACES:
			if space in message:
				return True
		return False