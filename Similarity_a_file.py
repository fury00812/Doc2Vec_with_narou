'''
文ごとに改行で区切った一つのファイルを使用して学習するモデル。
'''
import funcs_treatData as tdata
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from pathlib import Path

training_docs = []
lines = tdata.getLinesFromTxt('works/Renai_unreal/声を出さないと、決めました!!_edit') #作品の行リスト
print('文の数 ： '+str(len(lines)))
hinshi = ['名詞','動詞','形容詞','副詞']
i=0
for line in lines:
    token_list = tdata.getTokenlistFromline(line,hinshi)
    sent = TaggedDocument(words=token_list, tags=[i])
    training_docs.append(sent) #training_docsに対象文書を追加
    i+=1
model = Doc2Vec(vector_size=100, min_count=1, epochs=500)
model.build_vocab(training_docs)
model.train(training_docs, total_examples=model.corpus_count, epochs=model.epochs)

doc_id = 0
inferred_vector = model.infer_vector(training_docs[doc_id].words)
#infer_vector : 学習したモデルを用いてベクトル表現を算出
sims = model.docvecs.most_similar([inferred_vector],topn=10)
#topn=N トップNのみ返す

print('Document ({}): «{}»\n'.format(doc_id, lines[doc_id]))
for s in sims:
    print(s[1],lines[s[0]])
