import sys
import os
import random
import jieba

WordList = []
WordIDDic = {}

inpath = sys.argv[1]
OutFileName = sys.argv[2]
trainOutFile = open(OutFileName+".train", "w")
testOutFile = open(OutFileName+".test", "w")

# 创建停用词list函数
def stopwordslist(filepath):
    return [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  #返回一个列表，里面的元素是一个个的停用词

def seg_sentence(content:str):
    stopwords = stopwordslist(inpath + "stop.txt")
    seg_list = jieba.lcut(content)
    out_str = []
    for word in seg_list:
        if word not in stopwords:
            if word != '\t' and word != ' ':
                out_str.append(word)
    out_str = ' '.join(list(out_str))
    return out_str

def data_writer(path, counter):
    if str(path) == 'test':
        outfile = testOutFile
    
    if str(path) == 'training':
        outfile = trainOutFile

    path = inpath + str(path)
    for filename in os.listdir(path):
        if not filename.startswith('.'):  # 筛除 以 “.” 开头的隐藏文件
            label = filename[0]  # 读取标签
            counter += 1
            if counter % 100 == 0:
                print(counter, "files processed!\r")

            infile = open(path+'/'+filename, 'r', encoding='utf-8')  # 读取样本文章
            outfile.write(str(label)+" ")  # 先写标签
            content = infile.read().strip()  # 读取文章内容
            content = seg_sentence(content)  # 对文章内容分词

            words = content.replace('\n', ' ').split(' ')
            for word in words:
                if len(word.strip()) < 1:
                    continue
                if word not in WordIDDic:  # 如果该词语没有出现过
                    WordList.append(word)  # 将这些新登陆词存进一个列表里
                    WordIDDic[word] = len(WordList)  # 赋给这个新登陆词一个 id, 并存在字典里
                outfile.write(str(WordIDDic[word])+" ")
            outfile.write("#"+filename+"\n")
            infile.close()

    return counter

def ConvertData():
    i = 0
    i = data_writer("training", i)
    i = data_writer("test", i)

    print(i, "files loaded!")
    print(len(WordList), "unique words found!")

ConvertData()
trainOutFile.close()
testOutFile.close()



