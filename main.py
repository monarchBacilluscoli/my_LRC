from PIL import Image # 用于处理图像
import matplotlib.pyplot as plt # 用于处理绘图
import matplotlib.image as mpimg # 用于处理PNG格式图像
import numpy as np # 用于操作矩阵
import os # 用于展示系统参数

print(os.path.abspath('.'))


N = 2   #图片类数
Pi = 5  #每类图片张数

predictor = [] # 用于存储predictor的数组

# 读取N类图像并储存进变量之中
i=0
while i<N:
    j = 0
    path1 = "orl_faces\\s"+str(i+1)+"\\" # 第一层路径循环文件夹
    ims = [] # 初始化临时存储图片变量
    #读取一组图片到list中
    while j < Pi:
        # 读取一张图片
        path = path1+str(j+1)+".pgm" # 第二层路径循环图片文件
        im = Image.open(path) 
        # 将该图片插入到第j个predictor的一列中
        # ims.append(list(im.getdata()))  # 相对路径前面不用加\\
        ims.append(list(im.getdata()))
        print(ims[j][1000]) # 用于观察是不是导入了同一张图
        # 将一张图片插入predictor_i中
        # #print(ims[j].getdata())
        # data = list(ims[0].getdata())
        # print(len(data)) # 输出图片长度
        j = j+1

    # 将ims转换为predictor并插入到数组中
    p = np.array(ims[0]) # 先插入头一个图片
    j=1 # 此时j已经有一个
    # 将剩下的插入临时predictor
    while j<Pi-1:
        p = np.hstack((p,ims[j])) # 注意用法(一维数组不必加dtype)
    # 将predictor转置之后插入list
    predictor.append(p.T)
    i = i+1




# print(im.histogram()) # 输出直方图只是数据而已
# print(im)  # 输出文件有关信息、大小和色彩类型

# im.show()  # 显示图片

# 切割并显示图片
# box = (0, 0, 50, 100)  # 元组
# region = im.crop(box)
# print(region)
# region.show()

# 可能下采样函数要我自己写了，先不管这个事，先直接用。
