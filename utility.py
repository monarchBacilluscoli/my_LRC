
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

#我怀疑上面的标准化函数可能有问题
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

    