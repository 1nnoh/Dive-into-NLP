import sys
import math

docs_cnt = 508

current_word = None
count = 0

for line in sys.stdin:
    ss = line.strip().split('\t')
    if len(ss) != 2:
    
        continue
    word, val = ss
    if current_word == None:
        current_word = word

    if current_word != word:
        idf = math.log10(docs_cnt / (float(count) + 1.0))
        print('\t'.join([current_word, str(idf)]))
        count = 0  # 重置 count
        current_word = word  # 换到下一个 word

    count += int(val)

# 防止最后一类只有一行，导致最后一类没有输出
idf = math.log10(docs_cnt / (float(count) + 1.0))
print('\t'.join([current_word, str(idf)]))

