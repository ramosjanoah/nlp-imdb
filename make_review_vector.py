import read_dataset as read_dataset
import numpy as np
import gensim
import dill
from nltk.corpus import stopwords
from gensim.models.word2vec import Word2Vec

set_of_unknown_words = set()
stopword_set = set(stopwords.words('english'))

google_word2vec_path = "model/GoogleNews-vectors-negative300.bin"

def get_review_vector(model_word2vec, tokenized_review, size, pass_key_error=True, remove_stopwords=True):
	global set_of_unknown_words 
	global stopword_set
	# TOKENIZED REVIEW IS LIST OF TOKEN
	# FS : Get vector of review

	review_vector = np.zeros(shape=size)
	
	if not remove_stopwords:
		if pass_key_error:
			for token in tokenized_review:
				try:
					review_vector += model_word2vec.wv[token]
				except KeyError:
					#print(token)
					set_of_unknown_words.add(token)
					pass        
			review_vector = review_vector/len(tokenized_review)
		else: 
			for token in tokenized_review:
				review_vector += model_word2vec.wv[token]
			review_vector = review_vector/len(tokenized_review)        
	else:
		if pass_key_error:
			for token in tokenized_review:
				if token not in stopword_set:
					try:
						review_vector += model_word2vec.wv[token]
					except KeyError:
						#print(token)
						set_of_unknown_words.add(token)
						pass        
			review_vector = review_vector/len(tokenized_review)
		else: 
			for token in tokenized_review:
				if token not in stopword_set:
					review_vector += model_word2vec.wv[token]
			review_vector = review_vector/len(tokenized_review)        		

	return review_vector


def load_google_word2vec_model(filename, limit=500000):
	
	model = gensim.models.KeyedVectors.load_word2vec_format(limit=limit,
															 fname=filename,
															 binary=True)
	return model

# saving vector of review
def save_vector_of_reviews(model_word2vec, testtrain, posneg, size, window, min_count, stopwords=True):
	global set_of_unknown_words

	# reviews = read_dataset.load('data/structured/review_neg_handled/{}/{}.pkl'.format(testtrain, posneg))

	# review_vectors = []
	
	# for review in reviews:
	# 	review_vector = get_review_vector(model_word2vec, review, size=size, pass_key_error=True)
	# 	review_vectors.append(review_vector)
	review_vectors = "Haha"

	print("Saving Vector..")
	if stopwords:
		stopwords_str = "_stopwords"
	else:
		stopwords_str = ""        
	with open("data/structured/vector{}_{}_{}_{}/{}/{}.pkl".format(size, window, min_count, stopwords_str, testtrain, posneg), "wb") as fo:
		dill.dump(review_vectors, fo)
	print("Done.")

def testing():
	test_review = read_dataset.load("data/structured/vector/train/pos.pkl")        
	print(test_review)
	
if __name__ == '__main__':

	sizes = [100, 300]
	windows = [7,15]
	min_counts = [1, 3, 7, 15]
	stopwords = [True, False]

	for stopword in stopwords:		
		for size in sizes:
			for window in windows:
				for min_count in min_counts:	
						set_of_unknown_words = set()    
						model_filename = "model/model{}_{}_{}.pkl".format(size, window, min_count)
							
						model_word2vec = Word2Vec.load(model_filename)
						save_vector_of_reviews(model_word2vec, "train", "pos", size, window, min_count)
						save_vector_of_reviews(model_word2vec, "train", "neg", size, window, min_count)
						save_vector_of_reviews(model_word2vec, "test", "pos", size, window, min_count)    
						save_vector_of_reviews(model_word2vec, "test", "neg", size, window, min_count)
						with open("data/structured/vector{}_{}_{}_{}/unknown_words.pkl".format(size, window, min_count, stopwords_str), "wb") as fo:
							dill.dump(set_of_unknown_words, fo)					
					
	
	
	
	
	
	
	
	
	