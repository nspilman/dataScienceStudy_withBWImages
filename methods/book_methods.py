

# Chapter3
## Vectors
# 
 
from typing import List
Vector = List[float]
def add(v:Vector,w:Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i+w_i for v_i,w_i in zip(v,w)]

def subtract(v:Vector,w:Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i-w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors:List[Vector]) -> Vector:
    assert vectors, "no vectors provided"
    number_elements = len(vectors[0])
    assert all(len(v) == number_elements for v in vectors), "your vectors aren't all the same length"
    return [sum(vector[i] for vector in vectors) for i in range(number_elements)]

def scalar_multiply(c:float,v:Vector) -> Vector:
    return [c * v_i for v_i in v]

def vector_mean(vectors:List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v:Vector, w:Vector) -> Vector:
    assert len(v) == len(w), "your vectors aren't the same size"
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v:Vector):
    return dot(v,v)

import math
def magnitude(v:Vector) -> float:
    return math.sqrt(sum_of_squares(v))

def distance(v:Vector, w:Vector) -> float:
    return magnitude(subtract(v,w))

#Chapter 4
## Matrices 
Matrix = List[List[float]]
from typing import Tuple

def shape(A:Matrix) -> Tuple:
    num_rows = len(A)
    num_cols = len(A[0])
    return num_rows,num_cols
    
def get_row(A: Matrix, i:int) -> Vector:
    return A[i]

def get_column(A: Matrix, j:int) -> Vector:
    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_rows:int,
                num_cols:int,
                entry_fn:Callable
                ) -> Matrix:
                return [[entry_fn(i,j) for j in range(num_cols)]
                for i in range(num_rows)]