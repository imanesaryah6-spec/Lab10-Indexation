import numpy as np

A = np.array([10, 20, 30, 40, 50])
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

x = A[2]
y = M[0, 2]

print(x)
print(y)

t1 = A[1:4]
print(t1)

t2 = M[:2, 1:]
print(t2)

m_inv = M[::-1, :]
print(m_inv)

b = M[:2, :2].copy()
b[0, 0] = 999
print(M)

b_ex = M[:2, :2].copy()
b_ex[0, 0] = 999

A[1:-1] = 0
print(A)
