""" Testing file for df_util """

from functions import five_mult, tri_recursion, sum_two_numbers 
import unittest

#my class test functions

class FuncTests(unittest.TestCase):
    """Tests for my functions"""
    # all test methods be named test_***
    def test_five_mult3(self):
        self.assertEqual(five_mult(3),15)
    
    def test_recursive_3(self):
        self.assertEqual(tri_recursion(3),6)

    def test_sum_46_fail(self):
        self.assertNotEqual(sum_two_numbers(4,6),12)
    
    def test_sum_46_ok(self):
        self.assertEqual(sum_two_numbers(4,6),10)

# A command-line program that runs a set of tests; 
# this is primarily for making test modules conveniently executable. 
# The simplest use for this function is to include the following line at the end of a test script
if __name__ == '__main__':
    unittest.main()
