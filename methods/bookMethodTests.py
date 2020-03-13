from book_methods import *

# Chapter3
## Vectors
assert add([1, 2, 3],[4, 5, 6]) == [5,7,9]  
assert subtract([5,7,9],[4,5,6]) == [1,2,3]
assert vector_sum([[1,2,3],[4,5,6],[7,8,9]]) == [12,15,18]
assert scalar_multiply(2,[1,2,3]) == [2,4,6]
assert vector_mean([[1,2,3],[4,5,6],[7,8,9]]) == [4,5,6]
assert dot([1,2,3],[4,5,6]) == 32
assert sum_of_squares([2,4,6]) == 56
assert magnitude([3,4]) == 5

## Matrices

test_matrix = [
    [1,2,3],
    [4,6,8],
    [10,20,30],
    [100,200,300],
]
assert shape(test_matrix) == (4,3)
assert get_row(test_matrix,1) == test_matrix[1]
assert get_column(test_matrix,0) == [1,4,10,100]