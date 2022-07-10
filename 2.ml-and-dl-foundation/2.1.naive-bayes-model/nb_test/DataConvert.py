import sys
import os
import random

WordList = []
WordIDDic = {}
TrainingPercent = 0.8

inpath = sys.argv[1]
OutFileName = sys.argv[2]
trainOutFile = open(OutFileName+".train", "w")
testOutFile = open(OutFileName+".test", "w")

def ConvertData():
    i = 0
    tag = 0
    for filename in os.listdir(inpath):
        if not filename.startswith('.'):  # 筛除 以 “.” 开头的隐藏文件
            if filename.find("business") != -1:
                tag = 1  # 分配标签
            elif filename.find("auto") != -1:
                tag = 2
            elif filename.find("sport") != -1:
                tag = 3
            i += 1
            # 划分数据集
            rd = random.random()
            outfile = testOutFile
            if rd < TrainingPercent:
                outfile = trainOutFile

            if i % 100 == 0:
                print(i,"files processed!\r")

            infile = open(inpath+'/'+filename, 'r', encoding='utf-8')
            outfile.write(str(tag)+" ")  # 先写标签
            content = infile.read().strip()
            #content = content.decode("utf-8", 'ignore')
            words = content.replace('\n', ' ').split(' ')
            for word in words:
                if len(word.strip()) < 1:
                    continue
                if word not in WordIDDic:  # 如果该词语没有出现过
                    WordList.append(word)  # 将这些新登陆词存进一个列表里
                    WordIDDic[word] = len(WordList)  # 赋给这个新登陆词一个 id
                                                     # 并存在字典里
                outfile.write(str(WordIDDic[word])+" ")
            outfile.write("#"+filename+"\n")
            infile.close()

    print(i, "files loaded!")
    print(len(WordList), "unique words found!")

ConvertData()
trainOutFile.close()
testOutFile.close()
