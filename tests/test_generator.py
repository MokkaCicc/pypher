#!usr/bin/env python

import unittest

from pypher import Generator


class TestGenerator(unittest.TestCase):

    def test_shifted_alpha(self):
        shifted_alpha_ref = "defghijklmnopqrstuvwxyzabc"
        shifted_alpha = Generator.shifted_alpha(3)
        print('test')
        self.assertEqual(shifted_alpha_ref, shifted_alpha)


if __name__ == "__main__":
    unittest.main()