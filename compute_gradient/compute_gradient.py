import numpy as np

## version 1
# A = np.array([[2,3,4],[2,2,5],[1,3,4]]);
# B = np.dot(A,A)+np.eye(3)
# C = np.sum(A+B)/9

# delta = 0.001
# A1 = np.array([[2,3,4],[2,2,5],[1,3,4+delta]]);
# B1 = np.dot(A1,A1)+np.eye(3)
# C1 = np.sum(A1+B1)/9

# gradient = (C1-C)/(delta)

# print(A)
# print(B)
# print(C)
# print(C1)
# print(gradient)


## version 2
from sympy import *
a11,a12,a13,a21,a22,a23,a31,a32,a33 = symbols('a11 a12 a13 a21 a22 a23 a31 a32 a33')
A = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
B = np.dot(A,A)+np.eye(3)
C = np.sum(A+B)/9

grad = np.array([[diff(C,a11),diff(C,a12),diff(C,a13)],[diff(C,a21),diff(C,a22),diff(C,a23)],[diff(C,a31),diff(C,a32),diff(C,a33)]])

# print(grad)

f_grad = lambdify((a11,a12,a13,a21,a22,a23,a31,a32,a33),grad,'numpy')
# print(f_grad)
result = f_grad(2,3,4,2,2,5,1,3,4)
print(result)