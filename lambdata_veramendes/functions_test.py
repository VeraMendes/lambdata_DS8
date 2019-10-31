""" Testing file for df_util """

from functions import five_mult, tri_recursion, sum_two_numbers 
import unittest

#my class test functions

class FuncTests(unittest.TestCase):
    """Tests for my functions"""
    def test_five_mult3(self):
        self.assertEqual(five_mult(3),15)
    
    def recursive0(self):
        self.assertEqual(tri_recursion(0),0)

    def test_sum_46(self):
        self.assertNotEqual(sum_two_numbers(4,6),12)

if __name__ == '__main__':
    unittest.main()
