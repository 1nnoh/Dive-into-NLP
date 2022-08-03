import random
import numpy as np
import matplotlib.pyplot as plt

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

''' 随机梯度下降法 得到的最佳回归系数 '''
def sgd(data,label):
    datamat = np.mat(data)
    labelmat = np.mat(label).transpose()
    m, n = datamat.shape
    weight = np.ones((n,1))  # 创建与列数相同的矩阵的系数矩阵
    iters = 200
    for i in range(iters):
        dataindex = list(range(m))  # 返回 [0, 1, 2, ..., m] 的列表作为 index
        for j in range(m):
            learn_rate=4/(i+j+1)+0.01
            # 随着轮数的增加，学习率（或步长）逐渐变小
            randinx = int(random.uniform(0,len(dataindex)))  # 随机取一个 index
            # random.uniform(x, y) 随机生成一个实数，它在[x,y]范围内
            out = sigmoid(datamat[randinx]*weight)  # 计算预测值
            error = labelmat[randinx] - out  # 计算预测值与真实值的误差
            weight = weight + learn_rate  *  datamat[randinx].T * error  # 更新 w
            del(dataindex[randinx])
            # 学完一个样本，删除掉一个
    return weight.getA()

''' 数据可视化展示 '''
def plotBestFit(dataArr, labelMat, weights):
    n = np.shape(dataArr)[0]
    xcord1, xcord2, ycord1, ycord2 = [],[],[],[]
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    """
    dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
    w0*x0+w1*x1+w2*x2=f(x)
    x0最开始就设置为1， x2就是我们画图的y值，而f(x)被我们磨合误差给算到w0,w1,w2身上去了
    所以： w0+w1*x+w2*y=0 => y = (-w0-w1*x)/w2
    """
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

if __name__ == '__main__':
    # 1.加载数据
    datamat, labelmat = loaddata('testSet.txt')
    # 2.训练模型，f(x)=a1*x1+b2*x2+..+nn*xn 中 (a1,b2, .., nn).T 的矩阵值
    weight = sgd(datamat, labelmat)
    print(weight)
    # 3.数据可视化
    dataArr = np.array(datamat)
    plotBestFit(dataArr, labelmat, weight)

