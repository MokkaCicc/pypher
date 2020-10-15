#!usr/bin/env python

import unittest

from pypher import Generator


class TestGenerator(unittest.TestCase):
    def test_shifted_alpha_lower(self):
        shifted_alpha_ref = "defghijklmnopqrstuvwxyzabc"
        shifted_alpha = Generator.shifted_alpha(3)
        self.assertEqual(shifted_alpha_ref, shifted_alpha)

    def test_shifted_alpha_upper(self):
        shifted_alpha_ref = "DEFGHIJKLMNOPQRSTUVWXYZABC"
        shifted_alpha = Generator.shifted_alpha(3, upper=True)
        self.assertEqual(shifted_alpha_ref, shifted_alpha)

    def test_shifted_alpha_reverse(self):
        shifted_alpha_ref = "xyzabcdefghijklmnopqrstuvw"
        shifted_alpha = Generator.shifted_alpha(3, reverse=True)
        self.assertEqual(shifted_alpha_ref, shifted_alpha)


if __name__ == "__main__":
    unittest.main()