#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

m_a = [[1, 2], [3, 4]]
m_b = [[5, 6], [7, 8]]

print(matrix_mul(m_a, m_b))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
