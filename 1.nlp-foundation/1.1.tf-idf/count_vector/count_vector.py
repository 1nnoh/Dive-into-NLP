texts = ["He is a boy", "She is a girl, good girl"]

word_set = set()

# 存储词典
for text in texts:
    for word in text.strip().split(' '):
        word_set.add(word.strip(','))

print(word_set)

# 给词典中所有词语赋一个 id 值
word_id_dict = {}
for word in enumerate(word_set):
    word_id_dict[word[1]] = word[0]

print(word_id_dict)

# 根据上一步生成的 word_id_dict，将文档 texts 中的词语替换成对应的 id 
res_list = []

for text in texts:
    t_list = []
    for word in text.strip().split(' '):
        word = word.strip(',')
        if word in word_id_dict:
            t_list.append(word_id_dict[word])
    res_list.append(t_list)

print(res_list)

# 将文档 texts 转为向量
# tests 中有两个文档，每个文档的向量长度为词典长度
# 根据 word_id_dict，出现的词语在 id 对应的列表位置 +1
for res in res_list:
    result = [0] * len(word_set)
    for word_id in res:
        result[word_id] += 1

    print(result)
