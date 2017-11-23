#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:18:55 2017

@author: alson
"""

from keras.models import load_model
from keras.datasets import imdb
from keras.preprocessing import sequence
import numpy

# fix random seed for reproducibility
numpy.random.seed(7)

# load the dataset but only keep the top n words, zero the rest
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)

# truncate and pad input sequences
max_review_length = 500
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

print("loading")
model = load_model('LSTM_CNN_dropout_100_1_tanh')

# Predict
tp = 0
fp = 0
tn = 0
fn = 0
y_preds = model.predict(X_test)
for i, y in enumerate(y_test):
    y_pred = 0
    if y_preds[i] > 0.5:
        y_pred = 1
    else:
        y_pred = 0
    
    if y_pred == y:
        if y_pred == 1:
            tp+=1
        else:
            tn+=1
    else:
        if y_pred == 1:
            fp+=1
        else:
            fn+=1

print('tp:', tp)
print('tn:', tn)
print('fp:', fp)
print('fn:', fn)

accuracy = float(tp + tn) / float(tp + tn + fp + fn)
precision = tp / float(tp + fp)
recall = tp / float(tp + fn)
f1 = 2 * (precision * recall / float(precision + recall))

print('precision', precision)
print('recall', recall)
print('f1', f1)
print('accuracy', accuracy)