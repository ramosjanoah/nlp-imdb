import multiprocessing
import dill
import nltk
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.word2vec import LineSentence
from gensim.models.word2vec import Word2Vec

if __name__ == '__previous_main___': #edited by ramos
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
    
if __name__ == '__main__': #created by ramos

    # initiate list    

	pos = []
	neg = []
	all_data = []
    
    # load all data sentence

	with open('data/structured/sentence_neg_handled/train/pos.pkl', 'rb') as fi:
		sentence_train_pos = dill.load(fi)
	with open('data/structured/sentence_neg_handled/train/neg.pkl', 'rb') as fi:
		sentence_train_neg = dill.load(fi)
     
    # join the data    
	all_data = sentence_train_pos + sentence_train_neg 
	model_word2vec  = Word2Vec(all_data, size=100, window=7, min_count=7, workers=4)

    # filename to save (or load)			
	fname = "model/100-ver2.pkl"
    
    # check model
	print(model_word2vec.wv['good'])    
    
    # save the file in fname    
	model_word2vec.save(fname)