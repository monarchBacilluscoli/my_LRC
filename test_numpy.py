# numpy测试代码

import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

mt1 = np.array([a, b, c], dtype=int)  # 这个完美解决ndarray之中存储的是list的问题，但是要求每行长度相等
print(mt1)
mt1.transpose()
print("转置后", mt1)


mt2 = np.array([[1.0, 2.0], [3.0, 4.0]]).transpose()
print(mt2)
mt2.transpose()
print(mt2.transpose())  # 该矩阵的转置矩阵，这里的transpose()并不是modification函数，所以不会修改原始数据

mt3 = np.vstack((a, b))
print(mt3)
mt3 = np.vstack((mt3,c))
print(mt3)

mt0 = np.array(a)
print(mt0)