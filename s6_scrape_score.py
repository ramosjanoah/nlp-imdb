import scrape_lib as sl
import nltk
import negation_handling as neghandle
from sklearn.externals import joblib
from gensim.models.word2vec import Word2Vec
import importlib

import make_review_vector as mrv
importlib.reload(mrv)
importlib.reload(sl)


url_string = 'http://www.imdb.com/title/tt2304933/reviews' # 5th wave
url_string = 'http://www.imdb.com/title/tt2674426/reviews' # me before you
url_string = 'http://www.imdb.com/title/tt1815862/reviews' # after_earth
url_string = 'http://www.imdb.com/title/tt1670345/reviews' # now you see me
url_string = 'http://www.imdb.com/title/tt2948356/reviews' # Zootopia
url_string = 'http://www.imdb.com/title/tt0111161/reviews' # The Shawshank Redemption
url_string = 'http://www.imdb.com/title/tt0299930/reviews' # Gigli

def loadModel(filename):
        print("Load model from " + filename)
        clf = joblib.load(filename) 
        return clf

def score_imdb_url(url_string, **kwargs):
    scrape_limit = int(kwargs.get('scrape_limit', 100))

     #param
    size = 300
    window = 7
    min_count = 3

    if (kwargs.get('clf', 'svm') == 'svm'):
        # SVM
        clf = loadModel("/home/alson/Desktop/nlp-imdb/model/svm/model_svm_grid_300_7_3.pkl")
    else:
        # C-LSTM
        clf = 
                      

    model_filename = "/home/alson/Desktop/nlp-imdb/model/w2v/model{}_{}_{}.pkl".format(size, window, min_count)
    model_word2vec = Word2Vec.load(model_filename)

    reviews_raw= sl.scrapePages(url_string, scrape_limit)

    reviews = []

    for review_raw in reviews_raw:
        review = nltk.word_tokenize(review_raw[0])  
        review = neghandle.handling_negation_of_tokenized_sentence(review)         
        reviews.append(review)
  
    reviews_vector = []

    for review in reviews:
        reviews_vector.append(mrv.get_review_vector(model_word2vec, review, size=300))

    len(reviews_vector)

    reviews_class = clf.predict(reviews_vector)

    score = 0

    for review_class in reviews_class:
        score += review_class
        
    score = float(score)/len(reviews_class)    

    print("SCORE OF FILM : " + str(score*10))

    for i, review in enumerate(reviews_raw):
        print(review)
        print("Predict : " + str(reviews_class[i]))
        if int(review[1][0]) < 2 and reviews_class[i] == 0:
            break
    if (kwargs.get('clf', 'svm') == 'svm'):
        # SVM
        score = 1 - score
    return score