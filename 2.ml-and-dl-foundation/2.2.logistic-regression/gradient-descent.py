import numpy as np

''' sigmoid 跳跃函数 '''
def sigmoid(inX):
    return 1.0 / (np.exp(-inX) + 1)

''' 加载数据集和类标签 '''
def loaddata(filename):
    # dataMat 为原始数据， labelMat 为原始数据的标签
    datamat, labelmat = [], []
    fr = open(filename)
    for line in fr.readlines():
        linearr = line.strip().split('\t')
        datamat.append([1.0, float(linearr[0]), float(linearr[1])])  
        # 为了方便计算(将 b 放入矩阵一起运算)，在第一列添加一个 1.0 作为 x0
        # w^T x + b = [w1 w2]^T * [x1 x2] + b = [b w1 w2]^T * [1.0 x1 x2]
        labelmat.append(float(linearr[-1]))
    return datamat, labelmat

''' 梯度下降法 得到的最佳回归系数 '''
def gd(data, label):
    datamat = np.mat(data)  # 转换为 NumPy 矩阵 'matrix'
    labelmat = np.mat(label).transpose() # 首先将数组转换为 NumPy 矩阵，然后再将行向量转置为列向量
    # 转化为矩阵[[0,1,1,1,0,1.....]]，并转置[[0],[1],[1].....]
    # transpose() 行列转置函数
    # 将行向量转化为列向量   =>  矩阵的转置

    # m->数据量，样本数 n->特征数
    m,n = datamat.shape  # 矩阵的行数和列数
    # print(m,n)
    weight = np.ones((n,1))  # 初始化回归系数，这里 w 是列向量。 w^T 是行向量 [1 1 1]。
    iters = 200  # 迭代次数
    learn_rate = 0.001 # 步长

    for i in range(iters):
        # 因为根据公式，每次更新 w 需要对所有的数据 xi 做一个误差求和，
        # 然后乘以步长 learn_rate。所以这里都是对整个数据集矩阵做运算。
        # 所以说内存里要将所有数据都存放进来做运算
        # 也正是这个原因，GD 的运算速度会慢于 SGD。
        # SGD 每次迭代只随机取数据集中的一个样本。
        
        # wx:
        gradient = datamat*np.mat(weight)  # 矩阵乘法
        # sigmoid(w^T*x+b):
        out = sigmoid(gradient)  # 获得预测值
        # sigmoid(w^T*x+b) - yi:
        errors = labelmat - out  # labelmat 为真实值，相减得到误差

        # 更新回归系数 w := w - lr*grad(f(w)) 
        # 参考对 w 的求导，以及梯度更新的公式
        weight = weight + learn_rate * datamat.T * errors
        # 最后一项：
        # 0.001* (3*m)*(m*1) 即 步长*grad(w^Txi+b)*xi 的求和，得到 3*1 的列向量。
        # 得到的是对 m 列的对所有数据 x0，x1，x2 的偏移量求和。

    return weight.getA()  # .getA() 将矩阵转化为数组 'ndarray'

if __name__ == '__main__':
    datamat,labelmat = loaddata('testSet.txt')
    weight = gd(datamat,labelmat)
    print(weight)
