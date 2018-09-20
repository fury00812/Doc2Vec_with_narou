# ファイルについて------------------------------------------------------------------
## Doc2Vec_narou/Narou_collecter.py
  データの収集・加工プログラム。
  webサイト「小説家になろう」からデータを取得し、作品ごとに単文で分割しファイル出力する。

## Doc2Vec_narou/Similarity_a_file.py
  実行プログラム。一つのファイル（1作品)を使用して学習するモデル。

## Doc2Vec_narou/funcs_makeData,funcs_treatData
  データ収集、加工の機能をまとめた自作関数群。

## Doc2Vec_narou/works
  収集したなろう小説データ。

## doc2vec_lee.py
  web上のDoc2Vecチュートリアル。文書の類似度を計算する。

# 参考-----------------------------------------------------------------------
## 参考1 - Gensim Doc2Vecチュートリアル
https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/doc2vec-lee.ipynb

## 参考2 - B'zの歌詞について、dov2vecによる類似検索と、感情分析を行う
http://bci-blog.blogspot.com/2016/12/bzdoc2vec.html
