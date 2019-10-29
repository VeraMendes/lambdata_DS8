"""
lambdata - a colection of data science help functions
"""

import pandas as pd
import numpy as np 


#sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

#sample functions
def increment(x):
    return(x+1)

