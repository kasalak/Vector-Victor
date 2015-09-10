import math

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

""" Vector subtraction """
def vector_sub(v1, v2):
    if len(v1) != len(v2):
        raise ShapeException
    return [v1 - v2 for v1, v2 in zip(v1, v2)]

""" Vector sum of n vectors """

def vector_sum(v1, *args):

    return [sum(x) for x in zip(v1, *args)]

"""Vector multiplication by Scalar"""
def vector_multiply(v1,N):
    return [x * N for x in v1]

"""Dot product"""
def dot(v1, v2):
    if len(v1) != len(v2):
        raise ShapeException
    return sum([a*b for (a, b) in zip(v1, v2)])

"""Vector Mean"""
def vector_mean(*args):
    return [(sum(x)/len(args)) for x in zip(*args)]

"""Magnitude"""
def magnitude():
    return math.sqrt(dot(v1, v2))
