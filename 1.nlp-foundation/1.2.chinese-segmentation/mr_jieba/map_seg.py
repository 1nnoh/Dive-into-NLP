import os
import sys
from importlib import reload

os.system('tar xvzf jieba.tgz > /dev/null')

reload(sys)

sys.path.append("./")

import jieba
import jieba.posseg
import jieba.analyse

for line in sys.stdin:
    ss = line.strip().split('\t')
    if len(ss) != 2:
        continue
    music_id = ss[0].strip()
    music_name = ss[1].strip()

    seg_list = jieba.cut(music_name, cut_all=False)
    print('\t'.join([music_id, music_name, ' '.join(seg_list)]))

    #result_list = []
    #for x, w in jieba.analyse.extract_tags(music_name, withWeight=True):
        #result_list.append(':'.join([x, str(round(w, 3))]))

    #print music_name + " ==> " +' '.join(result_list)
