from PIL import Image  # 用于处理图像
import matplotlib.pyplot as plt  # 用于处理绘图
import numpy as np  # 用于操作矩阵
import utility as ut  # !在此选择归一化函数
from utility import normalize as normalize

N = 40  # 图片总类数
Pn = 10  # 每类图片的总数
Pi = 5  # 每类图片训练集张数
Pj = Pn - Pi  # 每类图片的预测集张数

# 重采样设置
# ? 重采样有没有个啥标准，这个样子比例关系很难弄啊
#! pillow中图像size表示是2-tuple: (width, height)
#! AT&T：(92, 112)
downsampling_size = (23, 28)

predictor = []  # 用于存储predictor的数组

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
        im = im.resize(downsampling_size, Image.BOX)  # 重采样
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
        p = np.vstack((p, ims[j]))  # 注意用法(一维数组不必加dtype)
        j += 1
    # 将predictor转置之后插入list
    predictor.append(p.T)
    i = i+1


# 创建一个N*Pj大小的存储隶属类别的数组
inner = []
belong = []
# 创建一个待拷贝的长度为Pj的内链表
for i in range(Pj):
    inner.append(0)
# 以内链表进行拷贝创建隶属类别链表
for i in range(N):
    belong.append(inner.copy())

# 将所有测试图片求取隶属类别
i = 0
while i < N:  # 外循环类别
    path1 = "orl_faces\\s"+str(i+1)+"\\"
    j = 0
    while j < Pj:  # 内层循环图片
        path = path1+str(j+Pi+1)+".pgm"  # 跳过前面Pi张训练图片
        test_im = Image.open(path)
        test_im = test_im.resize(downsampling_size, Image.BOX)  # 重采样
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
        belong[i][j] = dis.index(min(dis))+1
        j += 1
    i += 1
print(belong)
