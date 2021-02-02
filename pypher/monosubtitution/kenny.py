#!/usr/bin/env python

from abc import ABC, abstractclassmethod

from pypher import Converter


class Kenny(ABC):
	TRIGRAMME = {
		'A': "MMM",
		'B': "MMP",
		'C': "MMF",
		'D': "MPM",
		'E': "MPP",
		'F': "MPF",
		'G': "MFM",
		'H': "MFP",
		'I': "MFF",
		'J': "PMM",
		'K': "PMP",
		'L': "PMF",
		'M': "PPM",
		'N': "PPP",
		'O': "PPF",
		'P': "PFM",
		'Q': "PFP",
		'R': "PFF",
		'S': "FMM",
		'T': "FMP",
		'U': "FMF",
		'V': "FPM",
		'W': "FPP",
		'X': "FPF",
		'Y': "FFM",
		'Z': "FFP"
	}


	@abstractclassmethod
	def __init__(cls):
		pass


	@classmethod
	def encrypt(cls, message: str) -> str:
		message = Converter.normalize(message)
		crypted_message = ""

		for letter in message:
			if letter == " ":
				crypted_message += " "
			else:
				crypted_message += cls.TRIGRAMME[letter]

		return crypted_message


	# TODO decrypt method
	@classmethod
	def decrypt(cls, crypted_message: str) -> str:
		pass