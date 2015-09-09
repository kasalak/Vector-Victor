class ShapeException(Exception):
    pass

"""
Create linear algebra functions that pass tests in linear_algebra_test.py
1. Vector addition
2. Vector subtraction
3. Vector multiplication by Scalar
4. Mean of multiple vectors
5. Dot product
6. magnitude
"""
"""Vector addition"""
def shape(vector):
    return (len(vector),)

"""Vector addition"""

def vector_add(vector1, vector2):
    return sum(vector1, vector2) 
