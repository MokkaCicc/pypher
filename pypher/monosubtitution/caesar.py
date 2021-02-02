#!/usr/bin/env python

from abc import ABC, abstractclassmethod
import collections

from pypher import utils


class Caesar(ABC):
	@abstractclassmethod
	def __init__(cls):
		pass

	# TODO: use Generator.shift_alpha().
	@classmethod
	def encrypt(cls,
		message: str,
		key: int,
		keep_spaces: bool = True,
		keep_capitals: bool = True,
		keep_specials: bool = False,
		reverse:bool = False,
		debug: bool = False
	) -> str:
		lower_alpha = list(utils.LOWER_ALPHA)
		upper_alpha = list(utils.UPPER_ALPHA)
		shift_lower_alpha = collections.deque(lower_alpha)
		shift_upper_alpha = collections.deque(upper_alpha)

		if reverse:
			shift_lower_alpha.rotate(key)
			shift_upper_alpha.rotate(key)
		else:
			shift_lower_alpha.rotate(-key)
			shift_upper_alpha.rotate(-key)

		shift_lower_alpha = list(shift_lower_alpha)
		shift_upper_alpha = list(shift_upper_alpha)

		if not keep_capitals:
			message = message.lower()

		crypted_message = ""
		for char in message:
			if char in utils.LOWER_ALPHA:
				char_index = lower_alpha.index(char)
				crypted_message += shift_lower_alpha[char_index]

			elif char in utils.UPPER_ALPHA:
				char_index = upper_alpha.index(char)
				crypted_message += shift_upper_alpha[char_index]

			elif keep_spaces and char in utils.SPACES: 
				crypted_message += char

			elif keep_specials and char not in utils.SPACES:
				crypted_message += char

		if debug:
			print(
				f"""Alpha""",
				f"""{lower_alpha}""",
				f"""Alpha shifted {key} time(s) from {'right to left' if reverse else 'left to right'}""",
				f"""{shift_lower_alpha}""",
				f""""""
				f"""Message         : {message}""",
				f"""Crypted message : {crypted_message}""",
				sep="\n"
			)

		return crypted_message


	# TODO: implement decrypt
	@classmethod
	def decrypt(cls, crypted_message: str, key: int) -> str:
		pass


	# TODO: implement bruteforce
	@classmethod
	def bruteforce(cls, crypted_message: str) -> dict[int, str]:
		pass

		# dict: {
		#   '1': "dnfslkjdfsq",
		#   '2': "ioueljkhcfc",
		#   '3': "xwbcvxcnbkd"
		# }