#!/usr/bin/env python

import unittest

from pypher import Analyser


class TestAnalyser(unittest.TestCase):
	MESSAGE = "This is a secret message"

	def test_ocurs_chars(self):
		ocurs_ref = {'S': 5.0, 'E': 4.0, 'A': 2.0, 'I': 2.0, 'T': 2.0, 'C': 1.0, 'G': 1.0, 'H': 1.0, 'M': 1.0, 'R': 1.0, 'B': 0.0, 'D': 0.0, 'F': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 'Q': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0}
		ocurs = Analyser.ocurs_chars(self.MESSAGE)
		self.assertEquals(ocurs_ref, ocurs)

		ocurs_percent_ref = {'S': 25.0, 'E': 20.0, 'A': 10.0, 'I': 10.0, 'T': 10.0, 'C': 5.0, 'G': 5.0, 'H': 5.0, 'M': 5.0, 'R': 5.0, 'B': 0.0, 'D': 0.0, 'F': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 'Q': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0}
		ocurs_percent = Analyser.ocurs_chars(self.MESSAGE, percent=True)
		self.assertEquals(ocurs_percent_ref, ocurs_percent)

		reverse_ocurs_ref = {'B': 0.0, 'D': 0.0, 'F': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 'Q': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0, 'C': 1.0, 'G': 1.0, 'H': 1.0, 'M': 1.0, 'R': 1.0, 'A': 2.0, 'I': 2.0, 'T': 2.0, 'E': 4.0, 'S': 5.0}
		reverse_ocurs = Analyser.ocurs_chars(self.MESSAGE, reverse=True)
		self.assertEquals(reverse_ocurs_ref, reverse_ocurs)


if __name__ == "__main__":
	unittest.main()
