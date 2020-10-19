#!usr/bin/env python

import unittest

from pypher import Generator


class TestGenerator(unittest.TestCase):
    def test_shifted_alpha(self):
        shifted_lower_alpha_ref = "defghijklmnopqrstuvwxyzabc"
        shifted_lower_alpha = Generator.shifted_alpha(3)
        self.assertEqual(shifted_lower_alpha_ref, shifted_lower_alpha)

        shifted_upper_alpha_ref = "DEFGHIJKLMNOPQRSTUVWXYZABC"
        shifted_upper_alpha = Generator.shifted_alpha(3, upper=True)
        self.assertEqual(shifted_upper_alpha_ref, shifted_upper_alpha)

        reverse_shifted_alpha_ref = "xyzabcdefghijklmnopqrstuvw"
        reverse_shifted_alpha = Generator.shifted_alpha(3, reverse=True)
        self.assertEqual(reverse_shifted_alpha_ref, reverse_shifted_alpha)


if __name__ == "__main__":
    unittest.main()
    