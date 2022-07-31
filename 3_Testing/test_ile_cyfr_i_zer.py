import unittest

from ile_cyfr_i_zer import count_digits


class TestCounter(unittest.TestCase):

    def test_count_not_none(self):
        number = 8
        check = count_digits(number)

        self.assertIsNotNone(check)

    def test_count1(self):
        number = 8
        check = count_digits(number)

        self.assertEqual(check, 1)

    def test_count_type(self):
        number = 8
        check = count_digits(number)

        self.assertIsInstance(check, int)
