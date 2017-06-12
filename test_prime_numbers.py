"""Code to test my_prime_numbers function"""
import unittest
from primenumbers import my_prime_numbers
class test_my_prime_numbers(unittest.TestCase):
    def test_for_correctness(self):
        self.assertTrue(3 in my_prime_numbers(10))
        self.assertTrue(5 in my_prime_numbers(10))
        self.assertTrue(7 in my_prime_numbers(10))
    def test_for_negative_numbers(self):
        self.assertRaises(ValueError,my_prime_numbers(-8),"only positive values")
    def test_non_zero_or_1_input(self):
        self.assertRaises(ValueError,my_prime_numbers(0),"only integers allowed")
        self.assertRaises(ValueError,my_prime_numbers(1),"only integers allowed")
    def test_output_type_is_list(self):
        self.assertTrue(isinstance(my_prime_numbers(10)),list)
    def test_2_is_prime(self):
        self.assertTrue(2 in my_prime_numbers(10))
if__name__ == '__main__':
    unittest.main()