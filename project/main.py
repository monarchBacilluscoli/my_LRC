from __future__ import division  # 将整数/整数=整数的除法改为真正的除法
from PIL import Image  # 用于处理图像
import matplotlib.pyplot as plt  # 用于处理绘图
import numpy as np  # 用于操作矩阵
from utility import normalize_gray as normalize  # !在此选择归一化函数

# 全局参数
N = 40  # 图片总类数
Pn = 10  # 每类图片的总数
Pi = 5  # 每类图片训练集张数
Pj = Pn - Pi  # 每类图片的预测集张数


# ? 重采样有没有个啥标准，这个样子比例关系很难弄啊
#! pillow中图像size表示是2-tuple: (width, height)
#! AT&T：(92, 112)
downsampling_sizes = [(round(92/40), round(112/40)), (round(92/30), round(112/30)), (round(92/20), round(112/20)), (round(92/10), round(112/10)),
                      (round(92/5), round(112/5)), (round(92/2), round(112/2)), (round(92/1), round(112/1))]  # 不同轮次的重采样数据

overall_info = {}  # 不同轮次的结果存储
sampling_type = Image.BOX  # 重采样类型

# 以不同重采样尺寸循环运行
# for downsampling_size in downsampling_sizes:
downsampling_size = (round(92/20), round(112/20))
# 循环实验参数
predictor = []  # 用于存储predictor的数组
info = {'total_recognition_accuracy': 0.}  # 存储结果

# 构建N个带有Pi个图片的predictor的数组
i = 0
while i < N:
    j = 0
    path1 = "orl_faces\\s"+str(i+1)+"\\"  # 第一层路径循环文件夹
    ims = []  # 初始化临时存储图片变量
    # 读取一组图片到list中
    while j < Pi:
        # 读取一张图片
        path = path1+str(j+1)+".pgm"  # 第二层路径循环图片文件
        im = Image.open(path)
        im = im.resize(downsampling_size, sampling_type)  # 重采样
        # 将该图片插入到该类数组中
        ims.append(list(im.getdata()))
        # 标准化
        normalize(ims[j])
        j += 1
    # 将ims转换为predictor并插入到数组中
    p = np.matrix(ims[0])  # 先插入头一个图片
    j = 1  # 此时j已经有一个
    # 将剩下的插入临时predictor
    while j < Pi:
        p = np.vstack((p, ims[j]))
        j += 1
    # 将predictor转置之后插入list
    predictor.append(p.T)
    i = i+1

# 创建一个N*Pj大小的存储隶属类别的数组
inner = []
result = []
# 创建一个待拷贝的长度为Pj的内链表
for i in range(Pj):
    inner.append(0)
# 以内链表进行拷贝创建隶属类别链表
for i in range(N):
    result.append(inner.copy())

# 将所有测试图片求取隶属类别
i = 0
while i < N:  # 外循环类别
    path1 = "orl_faces\\s"+str(i+1)+"\\"
    j = 0
    while j < Pj:  # 内层循环图片
        path = path1+str(j+Pi+1)+".pgm"  # 跳过前面Pi张训练图片
        test_im = Image.open(path)
        test_im = test_im.resize(downsampling_size, sampling_type)  # 重采样
        y = list(test_im.getdata())
        # 对y进行标准化
        normalize(y)
        # 转化为matrix并转置
        y = np.matrix(y).T
        dis = []
        for p in predictor:
            beta = np.dot(np.linalg.inv(np.dot(p.T, p)), np.dot(p.T, y))
            yhat = np.dot(p, beta)
            dis.append(np.sqrt(np.sum(np.square(y-yhat))))
        # 找到最小距离所在的索引位置，将之视作该图片从属的类别，记录之
        result[i][j] = dis.index(min(dis))+1
        j += 1
    i += 1
print(result)

#     recognition_accuracy = []
#     # 处理识别结果
#     type_index = 1
#     for type in result:
#         recognition_accuracy.append(0.)
#         for rec in type:
#             if rec == type_index:
#                 recognition_accuracy[type_index-1] += 1
#         recognition_accuracy[type_index -1] = recognition_accuracy[type_index-1]/Pj
#         info['total_recognition_accuracy'] += recognition_accuracy[type_index-1]
#         type_index += 1
#     info['total_recognition_accuracy'] /= N  # 平均识别率
#     # print("平均识别率：", recognition_accuracy)
#     # print("总识别率：", info['total_recognition_accuracy'])
#     run_key = downsampling_size[0]*downsampling_size[1]
#     overall_info[run_key] = info['total_recognition_accuracy']

# print(overall_info)

# # 数据成图
# plt.plot(overall_info.keys(),overall_info.values(),'-o')
# plt.show()