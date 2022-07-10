# -*- coding:utf-8 -*-

import sys
import math

class Node:
    def __init__(self, word):
        self.bestScore = 0.0
        self.bestPreNode = None
        self.len = len(word)
        self.word = word

class BiLM:
    def __init__(self, lexiconFile, biLMFile):
        self.wordNum = 0
        self.wordIDTable = {}
        self.unigramProb = []
        self.bigramProb = []
        self.unknownWordProb = 1.0
        infile = open(lexiconFile, 'r')
        sline = infile.readline().strip()
        self.maxWordLen  = 1
        while len(sline) > 0:
            #sline = sline.decode("gb2312")
            items = sline.split(' ')
            if len(items) != 2:
                print("Lexicon format error!")
                sline = infile.readline().strip()
                continue
            self.wordIDTable[items[0]] = int(items[1])
            if len(items[0]) > self.maxWordLen:
                self.maxWordLen = len(items[0])
            sline = infile.readline().strip()
        infile.close()
        infile = open(biLMFile, 'r')
        sline = infile.readline().strip()
        items = sline.split(' ')
        if len(items) == 2:
            self.wordNum = int(items[0])
        else:
            print("Bad format found in LM file!")
            sys.exit()
        sline = infile.readline().strip()
        for i in range(len(self.wordIDTable)):
            self.unigramProb.append(0.0)
            self.bigramProb.append({})
        self.unigramProb.append(0.0)
        self.bigramProb.append({})
        wid = 1
        while len(sline) > 0:
            items = sline.split(' ')
            self.unigramProb[wid] = float(items[1])
            i = 2
            while i < len(items):
                self.bigramProb[wid][int(items[i])] = float(items[i+1])
                i += 2
            sline = infile.readline().strip()
            wid += 1
        infile.close()
        print(len(self.wordIDTable),"words loaded")

    def GetScore(self, word1, word2):
        wid1 = -1
        wid2 = -1
        if word1 not in self.wordIDTable:
            return self.unknownWordProb
        wid1 = self.wordIDTable[word1]
        if word2 not in self.wordIDTable:
            return self.unigramProb[wid1]
        wid2 = self.wordIDTable[word2]
        if wid2 not in self.bigramProb[wid1]:
            return self.unigramProb[wid1]
        return self.bigramProb[wid1][wid2]

def CreateGraph(s):
    WordGraph = []
    #Start Node
    newNode = Node("")
    newNodeList = []
    newNodeList.append(newNode)
    WordGraph.append(newNodeList)

    for i in range(len(s)):
        WordGraph.append([])

    #End Node
    newNode = Node(" ")
    newNodeList = []
    newNodeList.append(newNode)
    WordGraph.append(newNodeList)

    #Other nodes
    for i in range(len(s)):
        j = myBiLM.maxWordLen
        if i+j > len(s):
            j = len(s)-i
        while j > 0:
            if s[i:i+j] in myBiLM.wordIDTable:
                newNode = Node(s[i:i+j])
                WordGraph[i+j].append(newNode)
            j -= 1
        if len(WordGraph[i+1]) < 1:
            print("Unknown character found!",i,s[i])
            sys.exit()
    return WordGraph

def ViterbiSearch(WordGraph):

    #for al in WordGraph:
        #print "==="
        #for a in al:
            #print a.word
            #print "-"
    #print len(WordGraph)
    #sys.exit()

    for i in range(len(WordGraph)-1):
        for curNode in WordGraph[i+1]:
            preLevel = i+1-curNode.len
            if preLevel < 0:
                print("running error!")
                sys.exit()
            preNode = WordGraph[preLevel][0]
            score = myBiLM.GetScore(preNode.word,curNode.word)
            score = preNode.bestScore + math.log(score)
            maxScore = score
            curNode.bestPreNode = preNode
            for j in range(1, len(WordGraph[preLevel])):
                preNode = WordGraph[preLevel][j]
                score = myBiLM.GetScore(preNode.word,curNode.word)
                score = preNode.bestScore + math.log(score)
                if score > maxScore:
                    curNode.bestScore = score
                    curNode.bestPreNode = preNode


def BackSearch(WordGraph):
    resultList = []
    curNode = WordGraph[len(WordGraph)-1][0].bestPreNode
    while curNode.bestPreNode != None:
        resultList.insert(0,curNode.word)
        curNode = curNode.bestPreNode
    return resultList


LexiconFile = "./WordDic.rm.txt"
BiLMFile = "./BiModel.rm.txt"
myBiLM = BiLM(LexiconFile, BiLMFile)

inputStr = u"南京市长江大桥"
#inputStr = u"欢迎大家跟火哥学算法"

WordGraph = CreateGraph(inputStr)

for NodeList in WordGraph:
    for Node in NodeList:
        print("CurNode Word: ", Node.word)


ViterbiSearch(WordGraph)
resultList = BackSearch(WordGraph)
for word in resultList:
    print(word,)

