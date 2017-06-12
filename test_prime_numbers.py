"""Code to test my_prime_numbers function"""
import unittest#import unittest module
from primenumbers import my_prime_numbers #import from primenumbers
class test_my_prime_numbers(unittest.TestCase): #define class thet inherits from unittest.TestCase class
    def test_for_correctness(self): #define function to test for correctness of value
        self.assertTrue(3 in my_prime_numbers(10))
        self.assertTrue(5 in my_prime_numbers(10))
        self.assertTrue(7 in my_prime_numbers(10))
    def test_for_negative_numbers(self):# define fuction to test for negative numbers
        self.assertRaises(ValueError,my_prime_numbers(-8),"only positive values")
    def test_non_zero_or_1_input(self): #Define function to test for zero and one input
        self.assertRaises(ValueError,my_prime_numbers(0),"only integers allowed")
        self.assertRaises(ValueError,my_prime_numbers(1),"only integers allowed")
    def test_output_type_is_list(self):#Define function to test type of outputed data
        self.assertTrue(isinstance(my_prime_numbers(10)),list)
    def test_2_is_prime(self): #define test to check if 2 is a prime number
        self.assertTrue(2 in my_prime_numbers(10))
if__name__ == '__main__':
    unittest.main()