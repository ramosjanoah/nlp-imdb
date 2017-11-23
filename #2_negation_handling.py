import re
from nltk.tokenize import word_tokenize
import read_dataset as read_dataset

import importlib
importlib.reload(read_dataset)

def review_to_sentences(review):
    # MENGUBAH REVIEW MENJADI LIST OF SENTENCE
    sentences_review = re.split("([.!] )", review)
    
    num_sentence = len(sentences_review)
    
    for index in range(0,num_sentence):
        if len(sentences_review[index]) <= 2:
            sentences_review[index-1] +=sentences_review[index]
            
    for index in range(0,num_sentence):
        try:
            if len(sentences_review[index]) <= 2:
                del sentences_review[index]
        except IndexError:
            break
    return sentences_review

def tokenize_sentence(sentence, is_handling_negation = True):
    # MELAKUKAN TOKENISASI TERHADAP SENTENCE
    # jika is_handling_negation = True, maka negasi di handle
    tokenized_sentence = word_tokenize(sentence)    
    
    if is_handling_negation:
        tokenized_sentence = handling_negation_of_tokenized_sentence(tokenized_sentence)

    return tokenized_sentence    

def handling_negation_of_tokenized_sentence(tokenized_sentence):        
    # MELAKUKAN HANDLING TERHADAP SENTENCE YANG SUDAH DI TOKENIZED
    negation_token = ["not", "n't", "no"]
    
    negated = False
    negation_handled_sentence = []
    
    for token in tokenized_sentence:
        if token in negation_token:
            negated = True
        else:
            if negated:
                negation_handled_sentence.append("not " + token)
            else:
                negation_handled_sentence.append(token)
            negated = False            
    return negation_handled_sentence            

def review_to_tokenized_sentences(review, is_handling_negation=True):
    # MELAKUKAN TOKENIZED REVIEW DARI AWAL (REVIEW -> SENTENCE -> TOKEN)
    sentences = review_to_sentences(review)
    tokenized_review = []
    for sentence in sentences:
        
        tokenized_sentence = tokenize_sentence(sentence, is_handling_negation)
        #print(tokenized_sentence)
        tokenized_review.append(tokenized_sentence)
    
    return tokenized_review


def testing_tokenize_review():
    # TESTING PURPOSE ONLY
    review = "Although I didn't like Stanley & Iris tremendously as a film, I did admire the acting! Jane Fonda and Robert De Niro are great in this movie. I haven't always been a fan of Fonda's work but here she is delicate and strong at the same time. De Niro has the ability to make every role he portrays into acting gold. He gives a great performance in this film and there is a great scene where he has to take his father to a home for elderly people because he can't care for him anymore that will break your heart. I wouldn't really recommend this film as a great cinematic entertainment, but I will say you won't see much bette acting anywhere."
    review_to_tokenized_sentences(review)
            
            
if __name__ == "__main__":
    # MAIN, MAKING NEGATION HANDLING
    # it is saved to data/structured/sentence_neg_handled/

    print("[PROCESS] : read_dataset.save_from_corpus_to_sent('train','pos')")
    read_dataset.save_from_corpus_to_sent("train","pos")

    print("[PROCESS] : read_dataset.save_from_corpus_to_sent('test','pos')")
    read_dataset.save_from_corpus_to_sent("test","pos")

    print("[PROCESS] : read_dataset.save_from_corpus_to_sent('train','neg')")
    read_dataset.save_from_corpus_to_sent("train","neg")

    print("[PROCESS] : read_dataset.save_from_corpus_to_sent('test','neg')")
    read_dataset.save_from_corpus_to_sent("test","neg")

    print("[PROCESS] : read_dataset.save_from_corpus('train','pos')")
    read_dataset.save_from_corpus("train","pos")

    print("[PROCESS] : read_dataset.save_from_corpus('test','pos')")
    read_dataset.save_from_corpus("test","pos")

    print("[PROCESS] : read_dataset.save_from_corpus('train','neg')")
    read_dataset.save_from_corpus("train","neg")

    print("[PROCESS] : read_dataset.save_from_corpus('test','neg')")
    read_dataset.save_from_corpus("test","neg")
    
    