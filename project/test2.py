from __future__ import division  # 将整数/整数=整数的除法改为真正的除法
from PIL import Image  # 用于处理图像
import matplotlib.pyplot as plt  # 用于处理绘图
import numpy as np  # 用于操作矩阵
from utility import normalize_gray as normalize  # !在此选择归一化函数

# 数据成图
r_box = {6: 0.16000000000000003, 9: 0.7100000000000001, 12: 0.7900000000000001, 16: 0.8450000000000001, 30: 0.8900000000000002, 56: 0.9250000000000002, 99: 0.9200000000000002, 396: 0.905}
r_lanczos = {6: 0.1, 9: 0.675, 12: 0.8150000000000002, 16: 0.8850000000000001, 30: 0.9200000000000002, 56: 0.915, 99: 0.915, 396: 0.905}
r_nearest = {6: 0.05, 9: 0.2399999999999999, 12: 0.3749999999999999, 16: 0.6050000000000001, 30: 0.7100000000000001, 56: 0.82, 99: 0.8500000000000002, 396: 0.8750000000000002}
r_box_minmax_norm = {6: 0.085, 9: 0.58, 12: 0.7500000000000002, 16: 0.8300000000000001, 30: 0.8850000000000001, 56: 0.915, 99: 0.915, 396: 0.9100000000000001}
r_lanczos_minmax_norm = {6: 0.065, 9: 0.5850000000000002, 12: 0.7700000000000002, 16: 0.8350000000000002, 30: 0.8949999999999999, 56: 0.905, 99: 0.9100000000000001, 396: 0.9000000000000001}
r_nearest_minmax_norm = {6: 0.07, 9: 0.22000000000000006, 12: 0.37500000000000006, 16: 0.5250000000000001, 30: 0.6800000000000003, 56: 0.8050000000000003, 99: 0.8450000000000003, 396: 0.8700000000000003}
# plt.plot(r_box.keys(),r_box.values(),'-.',r_lanczos.keys(),r_lanczos.values(),'-',r_nearest.keys(),r_nearest.values(),'--')

fig = plt.figure()

plt.plot(r_box.keys(),r_box.values(),'o-', label='BOX+255')
plt.plot(r_box_minmax_norm.keys(),r_box_minmax_norm.values(),'bo--', label='BOX+minmax')
plt.plot(r_lanczos.keys(),r_lanczos.values(),'*-', label = 'LANCZOS+255')
plt.plot(r_lanczos_minmax_norm.keys(),r_lanczos_minmax_norm.values(),'c*--', label = 'LANCZOS+minmax')
plt.plot(r_nearest.keys(),r_nearest.values(),'^-', label = 'NEAREST+255')
plt.plot(r_nearest_minmax_norm.keys(),r_nearest_minmax_norm.values(),'g^--', label = 'NEAREST+minmax')

plt.xlabel('Feature Dimension')
plt.ylabel('Recognition Accuracy')
plt.title('recognition accuracy with respect to feature dimension')
plt.axis([0,400,0,1])

plt.legend()
plt.grid()
plt.savefig("result.eps",format = "eps")
plt.show()