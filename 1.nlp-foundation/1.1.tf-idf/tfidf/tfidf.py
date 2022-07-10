import math
import pandas as pd

docA = "The cat sat on my face"
docB = "The dog sat on my bed"

bowA = docA.split(' ')
bowB = docB.split(' ')

wordSet = set(bowA).union(set(bowB))

wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)

for word in bowA:
    wordDictA[word] += 1

for word in bowB:
    wordDictB[word] += 1

#print(wordDictA)
#print(wordDictB)
print(pd.DataFrame([wordDictA, wordDictB]))

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)

    return tfDict

tfDictA = computeTF(wordDictA, bowA)
tfDictB = computeTF(wordDictB, bowB)

# IDF = log(语料库的文档总数 / (包含该词的文档数 + 1))
def computeIDF(docList):
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    print('N:', N)
    print(idfDict)

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N /( float(val)+1))
    
    return idfDict

idfs = computeIDF([wordDictA, wordDictB])
print(idfs)

def computeTFIDF(tfDict, idfs):
    tfidfDict = {}
    for word, val in tfDict.items():
        tfidfDict[word] = val * idfs[word]

    return tfidfDict

tfidfDictA = computeTFIDF(tfDictA, idfs)
tfidfDictB = computeTFIDF(tfDictB, idfs)

print(pd.DataFrame([tfidfDictA, tfidfDictB]))
