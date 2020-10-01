import numpy 
import pandas


class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """
        construction for complex numbers 
        complex numbers have a real and imaginary part
        """
        self.r = realpart #
        self.i = imagpart

def add(self, other_complex):
    self.r += other_complex.r
    self.i += other_complex.i 

num1 = complex(3, -5)
num2 = complex(2, 6)

num1.add(num2)
print(num1.r, num1.i)
