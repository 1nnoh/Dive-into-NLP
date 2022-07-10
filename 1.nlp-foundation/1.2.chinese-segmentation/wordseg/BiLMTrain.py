import sys

idDataFile = "./RenMinData.id.txt"
wordDicFile = "./WordDic.rm.txt"
biModelFile = "./BiModel.rm.txt"

WordIDTable = {}
BigramTableList = []
UnigramCountList = []
SmoothedProbList = []
TotalNum = 0

# 读取上一步制作的字典（格式为：词语 \t 对应id）
# 将字典读入 WordIDTable 中
infile = open(wordDicFile, 'r')
# 每次读取一行字典，每行字典格式为——左边是词语，右边为 id
# 即 words 中 words[0] 为词语，words[1] 为 id
s = infile.readline().strip()  
while len(s) > 0:
    #s = s.decode("gb2312")
    words = s.split(' ')
    if words[0] not in WordIDTable:
        WordIDTable[words[0]] = int(words[1])
    s = infile.readline().strip()
infile.close()
print("Reading word dic file finished!")
print("Total number of words:",len(WordIDTable))

for i in range(len(WordIDTable)+1):
    BigramTableList.append({})
    UnigramCountList.append(0)
    SmoothedProbList.append(0)

# 读取已经转为 id 表示的人民日报数据
infile = open(idDataFile, 'r')
# 每次读取一行，一行即为一篇文章
s = infile.readline().strip()
while len(s) > 0:
    words = s.split(' ')
    widlist = []
    TotalNum += len(words)  # 统计所有文章的总词量
    # 将当前文章的所有词存入 widlist
    for word in words:
        widlist.append(int(word))  # 文章中的 word 已经是 id，所以这里是 int
    # 遍历刚刚的 widlist 
    # 统计 count(word) 存入 UnigramCountList
    # 根据 wordid 在 UnigramCountList[wordid] 位置统计词频
    for wordid in widlist:
        UnigramCountList[wordid] += 1

    # 再遍历一次 widlist 
    for i in range(len(widlist)-1):
        tmpHT = BigramTableList[widlist[i]]
        if widlist[i+1] not in tmpHT:
            tmpHT[widlist[i+1]] = 1
        else:
            tmpHT[widlist[i+1]] += 1
    s = infile.readline().strip()
infile.close()
print("Reading id data file finished!")

#compute probabilities
for wid1 in range(1,len(WordIDTable)+1):
    SmoothedProbList[wid1] = 1/(float)(UnigramCountList[wid1] + len(WordIDTable))
    ht = BigramTableList[wid1]
    for wid2 in ht.keys():
        ht[wid2] = (float)(ht[wid2]+1) /(float)(UnigramCountList[wid1] +
                len(WordIDTable))  # 避免分子分母为零，所以分子 + 1，分母 + len
    UnigramCountList[wid1] = (float)(UnigramCountList[wid1])/(float)(TotalNum)

#save to file
outfile = open(biModelFile, 'w')
outfile.write(str(len(WordIDTable))+" "+str(TotalNum)+"\r\n")
for wid1 in range(1,len(WordIDTable)+1):
    outfile.write(str(UnigramCountList[wid1])+" ")
    outfile.write(str(SmoothedProbList[wid1]))
    ht = BigramTableList[wid1]
    for wid2 in ht.keys():
        outfile.write(" "+str(wid2)+" "+str(ht[wid2]))
    outfile.write("\r\n")
outfile.close()
print("Writing model file finished!")
