#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np
from collections import Counter

def predict(X, K, train_x, train_y):
    labels = []
    n = X.shape[0]
    print('test size = %d' % n)
    for i in range(n):
        if (i % 400) == 0:
            print('predict #%d' % i)
        x = X[i]
        det = (train_x - x)
        dist = np.linalg.norm(det, axis=1)
        index = dist.argsort()[:K]
        votes = train_y[index]
        counter = Counter(votes)
        label = counter.most_common()[0][0]
        labels.append(label)
    return np.array(labels)
