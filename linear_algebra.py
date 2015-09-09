class ShapeException(Exception):
    pass

"""
Create linear algebra functions that pass tests in linear_algebra_test.py
1. Vector addition
2. Vector subtraction
3. Vector multiplication by Scalar
4. Mean of multiple vectors
5. Dot product
6. magnitude"""

""" Vector shape """
def shape(vector):
    return (len(vector),)

""" Vector addition"""

def vector_add(v1, v2):

    if len(v1) != len(v2):
        raise ShapeException
    return [sum(x) for x in zip(v1, v2)]
