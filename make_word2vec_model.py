import multiprocessing
import dill
import nltk
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.word2vec import LineSentence
from gensim.models.word2vec import Word2Vec

if __name__ == '__main__':
	pos = []
	neg = []
	all_data = []
	with open('structured/train/filtered/words/pos.pkl', 'rb') as fi:
		pos = dill.load(fi)
	with open('structured/train/filtered/words/neg.pkl', 'rb') as fi:
		neg = dill.load(fi)
	all_data = pos + neg
	# model = Word2Vec(all_data, size=100, window=7, min_count=7, workers=4)

	data_train = []
	for datum in all_data:
		sentences = nltk.sentence_tokenize(datum)
			
	fname = "model/100.pkl"
	print(len(all_data))
	# model.save(fname)
	model = Word2Vec.load(fname)
	print(model.wv['good'])