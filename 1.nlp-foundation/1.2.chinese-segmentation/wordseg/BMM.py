import sys

WordDic = {}
MaxWordLen = 1

# 写入字典
# 并且找到词语最大长度
def LoadLexicon(lexiconFile):
    global MaxWordLen
    infile = open(lexiconFile, 'r', encoding='gb2312')
    s = infile.readline().strip()  # 每次读一行
    while len(s) > 0:  # 通过判断每行的长度，放在 while 循环里读完整个文件
        #s = s.decode("gb2312")
        WordDic[s] = 1  # 读到的每行的词，放入字典
        if len(s) > MaxWordLen:
            MaxWordLen = len(s)  # 记录词语最大长度
        s = infile.readline().strip()
    infile.close()

def BMM(s):
    global MaxWordLen
    wordlist = []
    i = len(s)  # 句子长度为 i，代表有 i 个字
    while i > 0:
        start = i - MaxWordLen  # 从后向前，以最大长度匹配
        if start < 0:
            start = 0
        while start < i:
            tmpWord = s[start:i]  # 框起来 start 到 i 的字
            if tmpWord in WordDic:
                wordlist.insert(0, tmpWord)  # 在字典中找到匹配的词，那么放入 wordlist
                break
            else:
                start += 1
        # 如果 start 一直向后移动，直到 i（句尾）还没有匹配的词
        # 那么将最后的一个字作为一个分词结果
        if start >= i:
            wordlist.insert(0, s[i-1:i])
            start = i - 1
        i = start  
        # 因为 start~i的字已经构成了分词结果
        # 所以下一次循环中，句尾坐标 i 重新赋值，左闭右开，所以不包括 start
    return wordlist

def PrintSegResult(wordlist):
    print("After word-seg:")
    for i in range(len(wordlist)-1):
        print(wordlist[i])
    print(wordlist[len(wordlist)-1])

LoadLexicon("./lexicon.txt")

inputStr = u"南京市长江大桥"

wordlist = BMM(inputStr)
PrintSegResult(wordlist)

