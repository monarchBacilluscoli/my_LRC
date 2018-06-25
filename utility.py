from PIL import Image

def normalize(list):
    '''
    一维列表标准化函数
    使用(list[i]/min)/(max-min)的方式进行标准化

    Parameters
    ----------
    list: 待标准化的一维list
    return
    ----------
    no return
    '''
    maximum = max(list)
    minimum = min(list)
    for i in range(len(list)):
        list[i] = (list[i] - minimum)/(maximum-minimum)
    return

#我怀疑上面的标准化函数可能有问题（不适用于确定位深的灰度图像）
def normalize_gray(list,max_depth = 255):
    '''
    灰度图像标准化函数
    使用list[i]/max_depth的方式进行标准化

    Parameters
    ----------
    list: 待标准化的一维list
    max_depth: 灰度图像的最大位深，默认为255

    return
    ----------
    no return
    '''
    for i in range(len(list)):
        list[i] = list[i]/max_depth
    return

# todo: 我需要处理什么样类型的数据呢？貌似pillow的数据也可以？
def downsampling(image,scalar,resample):
    '''
    图片下采样函数

    Parameters
    ----------
    image: 待下采样的二维数组（或别的什么）
    scalar: 下采样倍数
    resample: 重采样模式（来自PIL）

    return
    ----------
    下采样后的新的大小的数组
    '''
    # todo: 函数体
    # todo: 此处需要return一个新的数组
    return
    