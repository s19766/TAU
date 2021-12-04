# Damian Eggert s19766
# assertion used in tests: Equal, NotEqual, True

import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_add_two_positive_numbers(self):
        result = self.calc.addition(5, 10)
        self.assertEqual(15, result)

    def test_add_two_numbers(self):
        result = self.calc.addition(-2, 3)
        self.assertEqual(1, result)

    def test_add_two_negative_numbers(self):
        result = self.calc.addition(-2, -6)
        self.assertEqual(-8, result)

    def test_sub_two_numbers(self):
        result = self.calc.subtraction(14, 8)
        self.assertEqual(6, result)

    def test_multi_two_numbers(self):
        result = self.calc.multiplication(2, 4)
        self.assertEqual(8, result)

    def test_div_two_numbers(self):
        result = self.calc.division(20, 4)
        self.assertEqual(5, result)

    def test_add_two_float_numbers(self):
        result = self.calc.addition(1.5, 3.6)
        mess = f"{type(1.5)} a={1.5} | {type(3.6)} b={3.6} \n Both should be <class 'int'>"
        self.assertTrue(result, mess)

    def test_add_two_strings(self):
        result = self.calc.addition('5', '6')
        mess = f"{type('5')} a={'5'} | {type('6')} b={'6'} \n Both should be <class 'int'>"
        self.assertTrue(result, mess)

    def test_sub_two_positive_numbers(self):
        result = self.calc.subtraction(20, 4)
        self.assertNotEqual(0, result)

    def test_sub_two_negative_numbers(self):
        result = self.calc.subtraction(-4, -1)
        self.assertNotEqual(5, result)

    def test_multi_two_positive_numbers(self):
        result = self.calc.multiplication(10, 20)
        self.assertNotEqual(1, result)
