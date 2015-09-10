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
    return [sum(arg) for arg in zip(v1, v2)]

""" Vector subtraction """
def vector_sub(v1, v2):
    if len(v1) != len(v2):
        raise ShapeException
    return [v1 - v2 for v1, v2 in zip(v1, v2)]

""" Vector sum of n vectors """

def vector_sum(*args):
    for arg in args:
        if len(arg) != len(args[0]):
            raise ShapeException
    return [sum(arg) for arg in zip(*args)]

"""Vector multiplication by Scalar"""
def vector_multiply(vec,sca):
    return [arg * sca for arg in vec]

"""Dot product"""
def dot(v1, v2):
    if len(v1) != len(v2):
        raise ShapeException
    return sum([a*b for (a, b) in zip(v1, v2)])

"""Vector Mean"""
def vector_mean(*args):
    return [(sum(arg)/len(args)) for arg in zip(*args)]

"""Magnitude"""

def magnitude(vec):

    return  math.sqrt(dot(vec, vec))
