import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

texts = ['这只皮靴号码大了，那只号码合适','这只皮靴号码不小，那只更合适']

# 分词
texts_cut = []

def cut_word(sentence):
    return '/'.join(jieba.lcut(sentence))

for text in texts:
    #text = text.replace('，', '')
    texts_cut.append(cut_word(text))
    # strip() 只能移除字符串头尾指定的字符序列，不能删除中间部分的字符
print(texts_cut)
# 输出：分词结果
# ['这/只/皮靴/号码/大/了/，/那/只/号码/合适', '这/只/皮靴/号码/不小/，/那/只/更/合适']

# 创建词袋数据结构
# CountVectorizer参数中，默认的正则表达式选择2个及以上的字母或数字作为token
# 那么会导致分词为单个字的词语被忽略
# 所以这里需要修改正则表达式参数
cv = CountVectorizer(token_pattern=r"(?u)\b\w+\b")  # 修改正则表达式参数

cv_fit = cv.fit_transform(texts_cut)
# 上行代码等价于下面两行
# cv.fit(texts)
# cv_fit=cv.transform(texts)

# 列表形式呈现文章生成的词典
print(cv.get_feature_names())
# 输出：词典
# ['不小', '了', '只', '号码', '合适', '大', '更', '皮靴', '这', '那']

# 字典形式的词典，带有词语 id
print(cv.vocabulary_)
# 输出：
# {'这': 8, '只': 2, '皮靴': 7, '号码': 3, '大': 5, '了': 1, '那': 9, '合适': 4, '不小': 0, '更': 6}
# 字典形式，key：词，value:该词（特征）的索引，同时是tf矩阵的列号

# 所有文本的词频
print(cv_fit)
# 输出：
# (0, 8)  1  第 0 个文档中，词典索引为 8 的元素（这），词频为 1
# (0, 2)  2
# (0, 7)  1
# (0, 3)  2
# (0, 5)  1
# (0, 1)  1
# (0, 9)  1
# (0, 4)  1
# (1, 8)  1
# (1, 2)  2
# (1, 7)  1
# (1, 3)  1
# (1, 9)  1
# (1, 4)  1
# (1, 0)  1
# (1, 6)  1

# toarray() 将结果转为稀疏矩阵的表达
print(cv_fit.toarray())
# 输出：
# [[0 1 2 2 1 1 0 1 1 1]
#  [1 0 2 1 1 0 1 1 1 1]]

# 计算余弦相似度
texts_countvector = cv_fit.toarray()
cos_sim = cosine_similarity(texts_countvector[0].reshape(1,-1), texts_countvector[1].reshape(1,-1))
print('Cosine Similarity = %f'%cos_sim)

# 计算 jaccard 相似度
def jaccard_sim(a,b):
    unions = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return intersections / unions

print('Jaccard Similarity = %f'%jaccard_sim(texts_cut[0],texts_cut[1]))

# 计算欧氏距离相似度
# calculating Euclidean distance
# using linalg.norm()
point1 = texts_countvector[0]
point2 = texts_countvector[1]
dist = np.linalg.norm(point1 - point2)

print('Euclidean Distance = %f'%dist)


