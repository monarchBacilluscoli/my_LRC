from PIL import Image  # 用于处理图像
import matplotlib.pyplot as plt  # 用于处理绘图
import matplotlib.image as mpimg  # ! 用于处理PNG格式图像
import numpy as np  # 用于操作矩阵
import os  # ! 用于展示系统参数

print(os.path.abspath('.'))  # ! 输出文件所在位置


N = 10  # 图片总类数
Pn = 10  # 每类图片的总数
Pi = 5  # 每类图片训练集张数
Pj = Pn - Pi  # 每类图片的预测集张数

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
        # 将该图片插入到第j个predictor的一列中
        # ims.append(list(im.getdata()))  # 相对路径前面不用加\\
        ims.append(list(im.getdata()))
        # 标准化
        maximum = max(ims[j])
        minimum = min(ims[j])
        for index in range(len(ims[j])):
            ims[j][index] = (ims[j][index] - minimum)/(maximum-minimum)
        # print(ims[j][0])  # 用于观察是不是导入了同一张图
        # 将一张图片插入predictor_i中
        # #print(ims[j].getdata())
        # data = list(ims[0].getdata())
        # print(len(data)) # 输出图片长度
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
    # 输出一下看看
    # print(predictor[i])
    i = i+1



# 创建一个N*Pj大小的存储隶属类别的数组
inner = []
belong = []
# 创建一个待拷贝的长度为Pj的内链表
for i in range(Pj):
    inner.append(0)
# 以内敛表进行拷贝创建隶属类别链表
for i in range(N):
    belong.append(inner.copy())

# 将所有测试图片求取隶属类别
# 外循环类别
i = 0
while i < N:
    path1 = "orl_faces\\s"+str(i+1)+"\\"
    j = 0
    # 内层循环图片
    while j < Pj:
        path = path1+str(j+Pi+1)+".pgm"  # 跳过前面Pi张训练图片
        test_im = Image.open(path)
        y = list(test_im.getdata())
        # 对y进行标准化
        maximum = max(y)
        minimum = min(y)
        for index in range(len(y)):
            y[index] = (y[index] - minimum)/(maximum-minimum)
        # 转化为matrix并转置
        y = np.matrix(y).T
        dis = []
        for p in predictor:
            beta = np.dot(np.linalg.inv(np.dot(p.T, p)), np.dot(p.T, y))
            #print("beta: ", beta)
            yhat = np.dot(p, beta)
            #print("yhat: ", yhat)
            dis.append(np.sqrt(np.sum(np.square(y-yhat))))
        # todo: 找到最小距离所在的索引位置，将之视作该图片从属的类别，记录之
        #print(dis.index(min(dis))+1)
        belong[i][j] = dis.index(min(dis))+1
        #print(dis)
        #print(belong[i][j])
        j += 1
    i += 1
print(belong)


'''
# 读取一张图片并预测
# 读取一张图片并转化为y
path = "orl_faces\\s1\\6.pgm"  # 使用第七张图片进行预测
test_im = Image.open(path)
y = list(test_im.getdata())
# 对图片进行标准化
maximum = max(y)
minimum = min(y)
for index in range(len(y)):
    y[index] = (y[index] - minimum)/(maximum-minimum)
y = np.matrix(y).T
print(len(y))  # 确认转换是否正确
# 计算不同类predictor的y和yhat的距离
dis = []
for p in predictor:
    beta = np.dot(np.linalg.inv(np.dot(p.T, p)), np.dot(p.T, y))
    print("beta: ", beta)
    yhat = np.dot(p, beta)
    print("yhat: ", yhat)
    dis.append(np.sqrt(np.sum(np.square(y-yhat))))
print(dis)
'''
