""" A collection of data science helper function"""

import pandas as pd 
import numpy as np 



TEST = pd.DataFrame(np.ones(20))

def null(x):
    return (x.isnull().sum())


def sum(x):
   y = x.sum()
   return(y)
   