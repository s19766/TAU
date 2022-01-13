# Damian Eggert s19766
# assertion used in tests: Equal, NotEqual, True
# new assertion used in tests: GreaterEqual, Less, In

import unittest
from calculator import Calculator
import calculator_dependencies


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

    # --------------------------------------------
    # new tests
    def test_modulo_two_positive_numbers(self):
        result = self.calc.modulo(10, 3)
        self.assertEqual(1, result)

    def test_modulo_two_negative_numbers(self):
        result = self.calc.modulo(-20, -6)
        self.assertEqual(-2, result)

    def test_modulo_two_numbers(self):
        result = self.calc.modulo(215, -14)
        self.assertEqual(-9, result)

    def test_modulo_two_numbers_not_equal(self):
        result = self.calc.modulo(12, 12)
        self.assertNotEqual(2, result)

    def test_add_two_numbers_greater(self):
        result = self.calc.addition(15, -5)
        self.assertGreater(11, result)

    def test_multi_two_numbers_less(self):
        result = self.calc.multiplication(9, 7)
        self.assertLess(60, result)

    def test_div_two_numbers_greater_equal(self):
        result = self.calc.division(144, 12)
        self.assertGreaterEqual(12, result)

    # --------------------------------------------
    # dependencies tests
    def test_text(self):
        mess = "Hello You are using calculator"
        self.assertTrue(mess, calculator_dependencies.colored_text())

    def test_add(self):
        result = calculator_dependencies.add(5, 12)
        self.assertEqual(17, result)

    def test_word_in_string(self):
        word = "You"
        self.assertIn(word, calculator_dependencies.colored_text())
