import read_dataset as read_dataset
import negation_handling as neghandle
import numpy as np
import gensim
import nltk
import glob
import dill
from gensim.models.word2vec import Word2Vec


google_word2vec_path = "model/GoogleNews-vectors-negative300.bin"

def get_review_vector(model_word2vec, tokenized_review, pass_key_error=True):
    global set_of_unknown_words 
    # TOKENIZED REVIEW IS LIST OF TOKEN
    # FS : Get vector of review

    review_vector = np.zeros(shape=100)
    
    # default pass key error = True
    if pass_key_error:
        for token in tokenized_review:
            try:
                #print(token)
                #print(model_word2vec.wv[token])
                review_vector += model_word2vec.wv[token]
            except KeyError:
                print(token)
                set_of_unknown_words.add(token)
                pass        
        review_vector = review_vector/len(tokenized_review)
    else: #not default
        for token in tokenized_review:
            #print(token)
            #print(model_word2vec.wv[token])
            review_vector += model_word2vec.wv[token]
        review_vector = review_vector/len(tokenized_review)        

    return review_vector

def load_google_word2vec_model(filename, limit=500000):
    
    model = gensim.models.KeyedVectors.load_word2vec_format(limit=limit,
                                                           fname=filename,
                                                           binary=True)
    return model

# saving vector of review
def save_vector_of_reviews(model_word2vec, testtrain,posneg):
    global set_of_unknown_words

    reviews = read_dataset.load('data/structured/review_neg_handled/{}/{}.pkl'.format(testtrain, posneg))

    review_vectors = []
    
    for review in reviews:
        review_vector = get_review_vector(model_word2vec, review, pass_key_error=True)
        review_vectors.append(review_vector)

    print("Saving Vector..")
    with open("data/structured/vector/{}/{}.pkl".format(testtrain, posneg), "wb") as fo:
        dill.dump(review_vectors, fo)
    print("Done.")

def testing():
    test_review = read_dataset.load("data/structured/vector/train/pos.pkl")        
    print(test_review)
    
if __name__ == '__main__':
    set_of_unknown_words = set()    
    
    model_filename = "model/100-ver3.pkl"
    
    model_word2vec = Word2Vec.load(model_filename)
    
    save_vector_of_reviews(model_word2vec, "train", "pos")
    save_vector_of_reviews(model_word2vec, "train", "neg")
    save_vector_of_reviews(model_word2vec, "test", "pos")    
    save_vector_of_reviews(model_word2vec, "test", "neg")
    
    
    
    