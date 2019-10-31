"""
utility functions to work with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame([1,2,3,4,5,6])

def five_mult(x):
    return 5 * x 

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

def sum_two_numbers(a,b):
    return a + b
