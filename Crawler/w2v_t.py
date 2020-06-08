#w2v.py
import json
import pandas as pd

from gensim.models import word2vec

train_data = word2vec.LineSentence('/Users/tianyouwu/Desktop/fintech/ParsedData/Parsed0527_Text.txt')
model = word2vec.Word2Vec(
	train_data,
	min_count=5,
	size=100,
	workers=8,
	iter=5,
	window=10,
	sg=0,
	seed=666,
	batch_words=10000
)

model.save('word2vec.model')

model_try = word2vec.Word2Vec.load('word2vec.model')
#print(model_try['trump'].shape)
#每兩週推文模擬一次（還沒做好），並且把所有vocab丟進去算每個與其他字之間的關聯性取前十，
#再從這N個主體裡面的10個，總共10N去算其中出現最多次的字取前三，記下他的向量數值
word = []
for words in model_try.vocab.keys():
	most_similar = model_try.most_similar(words)
	word.append(words)
	x = []
	for item in most_similar:
		x.append(item[1])
	average.append(np.mean(x))
'''
data = pd.read_json('/Users/tianyouwu/Desktop/fintech/ParsedData/Parsed0527.txt')
data[['Text']].to_csv('/Users/tianyouwu/Desktop/fintech/ParsedData/Parsed0527_Text.txt')
'''


