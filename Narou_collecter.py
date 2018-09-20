'''
データをなろうから集める実行ファイル
'''

import funcs_makeData as mdata
import funcs_treatData as tdata
import os
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

#恋愛、ファンタジー、文芸
genres = {'Renai_unreal':101,'Renai_real':102,'Fantasy_high':201,'Fantasy_low':202,
            'Liter_pure':301,'Liter_human':302,'Liter_history':303,'Liter_reason':304,
            'Liter_horror':305,'Liter_action':306,'Liter_comedy':307}
for genre,num in genres.items():
    dicts = dict() #非日常恋愛ジャンルの作品URL辞書{タイトル:URL}
    dicts = mdata.getURLFromRank('https://yomou.syosetu.com/rank/genrelist/type/daily_'+str(num)+'/')
    #print(renai_unreal)

    for title,url in dicts.items(): #1ループ1作品
        textURL = mdata.getSectionFromURL(url) #各話のURLリスト
        path = 'works/'+genre+'/'+title #ファイルパス
        if os.path.isfile(path) != True:
            #os.remove(path) #一度ファイル削除
            f = open(path,'a')
            for url_Section in textURL: #1ループ1セクション
                text = mdata.getTextFromSection(url_Section) #各話のテキスト
                '''「。」で分割し、書き込み。全角空白は削る'''
                for line in text.split('。'):
                    line = line.replace('　','')
                    f.write(line+'\n')
            f.close()
