#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import re
import math
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

INPUT = """We could attack this problem the same way we attacked handwriting recognition - by using the pixels in the image as input to a neural network, with the output from the network a single neuron indicating either "Yes, it's a face" or "No, it's not a face".
Let's suppose we do this, but that we're not using a learning algorithm. Instead, we're going to try to design a network by hand, choosing appropriate weights and biases. How might we go about it? Forgetting neural networks entirely for the moment, a heuristic we could use is to decompose the problem into sub-problems: does the image have an eye in the top left? Does it have an eye in the top right? Does it have a nose in the middle? Does it have a mouth in the bottom middle? Is there hair on top? And so on.
If the answers to several of these questions are "yes", or even just "probably yes", then we'd conclude that the image is likely to be a face. Conversely, if the answers to most of the questions are "no", then the image probably isn't a face.
Of course, this is just a rough heuristic, and it suffers from many deficiencies. Maybe the person is bald, so they have no hair. Maybe we can only see part of the face, or the face is at an angle, so some of the facial features are obscured. Still, the heuristic suggests that if we can solve the sub-problems using neural networks, then perhaps we can build a neural network for face-detection, by combining the networks for the sub-problems. Here's a possible architecture, with rectangles denoting the sub-networks. Note that this isn't intended as a realistic approach to solving the face-detection problem; rather, it's to help us build intuition about how networks function. Here's the architecture:"""

# docs = [x.strip() for x in open('input')]
docs = [x.strip() for x in INPUT.split()]

def pp(docs):
    def f(x):
        x = re.sub('[^a-zA-Z]', ' ', x)
        words = x.lower().split(' ')
        words = [x for x in words if re.match(r'(?u)\b\w\w+\b', x)]
        return words
    docs = [f(x) for x in docs]
    return docs

docs = pp(docs)

def tfidf():
    word_dict = {}
    word_idx = 0
    for words in docs:
        for w in words:
            if w not in word_dict:
                word_dict[w] = word_idx
                word_idx += 1
    feature_names = list(word_dict.items())
    feature_names.sort(lambda x, y: cmp(x[1], y[1]))
    feature_names = [x[0] for x in feature_names]

    nw = len(word_dict)
    nd = len(docs)
    d = np.zeros((nd, nw))

    # counter
    for (idx, words) in enumerate(docs):
        for w in words:
            word_idx = word_dict[w]
            d[idx][word_idx] += 1

    # return d, feature_names
    # print d

    # norm counter. get df
    wv = d.sum(axis = 1)
    wv = wv[:, np.newaxis]
    d = d / wv

    # * idf
    idf_w = np.zeros(nw)
    for w in word_dict:
        word_idx = word_dict[w]
        has = 0
        for words in docs:
            if w in words:
               has += 1
        v = np.log(nd * 1.0 / (1 + has))
        idf_w[word_idx] = v

    d = np.multiply(d, idf_w)
    return d, feature_names

def tfidf2():
    # vectorizer = CountVectorizer(analyzer = 'word')
    vectorizer = TfidfVectorizer(analyzer = 'word', norm = None)
    d = vectorizer.fit_transform([' '.join(x) for x in docs])
    feature_names = vectorizer.get_feature_names()
    # print vectorizer.idf_
    return d, feature_names

if __name__ == '__main__':
    (d, fs) = tfidf()    
    (d2, fs2) = tfidf2()
    print d, d2
