import numpy as np

# Logistic函数
def logistic(wTx):
    return 1.0 / (1.0 + np.exp(-wTx))

# 分类函数
def classifier(testData, weights):
    prob = logistic(sum(testData*weights)) # 求取概率--判别算法
    if prob > 0.5:
        return 1.0 # prob>0.5 返回为1
    else:
        return 0.0 # prob<=0.5 返回为0

# 回归函数
def regression_calc(testData, weights):
    prob = logistic(sum(testData*weights)) # 求取概率--判别算法
    return prob

# predict
weights = np.mat([[4.17881308],[0.50489874],[0.61980264]])
testdata = np.mat([0.931635, -1.589505])

m, n = np.shape(testdata)
testmat = np.zeros((m,n+1))
# 添加个第一列作为 x0，方便计算，将 b 纳入矩阵计算。
testmat[:,0] = 1
# 后两列为原测试数据
testmat[:,1:] = testdata

print(classifier(testmat,weights))
print(regression_calc(testmat,weights))
