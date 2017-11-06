import glob
import nltk
import dill
from nltk.corpus import stopwords

def save_from_corpus(testtrain, posneg):
    reviews = []

    path = "data/{}/{}/*.txt".format(testtrain, posneg)
    files = glob.glob(path)
    for i, file in enumerate(files):
        if i % 100 == 0:
            print(i)
        with open(file, "r") as fi:
            review = fi.read()
        review = nltk.word_tokenize(review)
        review = nltk.pos_tag(review)
        reviews.append(review)
        
    # Masukin ke file
    print("Saving...")
    with open("data/structured/{}/{}.pkl".format(testtrain, posneg), "wb") as fo:
        dill.dump(reviews, fo)
    print(len(reviews))

def load(path):
    with open(path, 'rb') as fi:
        return dill.load(fi)

def get_filtered_sentence(tagged_sentence):
    filtered_tagged_sentence = []
    words, tags = zip(*tagged_sentence)
    for i, word in enumerate(words):
        if word not in stopwords.words('english'):
            filtered_tagged_sentence.append(tagged_sentence[i])
    return filtered_tagged_sentence

if __name__ == "__main__":
    # save_from_corpus("test", "pos")
    print(stopwords.words('english'))
    testtrain = "test"
    posneg = "pos"
    pos_reviews = load('data/structured/{}/{}.pkl'.format(testtrain, posneg))
    filtered_pos_reviews = []
    for i, pos_review in enumerate(pos_reviews):
        if i % 100 == 0:
            print(i)
        filtered_pos_review = get_filtered_sentence(pos_review)
        # print(filtered_pos_review)
        filtered_pos_reviews.append(filtered_pos_review)
    with open("data/structured/{}/filtered/{}.pkl".format(testtrain, posneg), "wb") as fo:
        dill.dump(filtered_pos_reviews, fo)
    print(len(filtered_pos_reviews))
