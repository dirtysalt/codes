#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


def fit(X, y, cb = None):
    np.random.seed(42)
    X = np.hstack((X, np.ones((X.shape[0], 1))))
    y = np.where(y == 1, 1, 0)
    print('X.shape = %s, y.shape = %s' % (X.shape, y.shape))

    (n_samples, n_features) = X.shape
    # w = np.zeros(n_features)
    w = np.random.randn(n_features)
    # print(w)

    batch = 100
    n_iter = 10000
    rate = 0.1

    delta_w = np.zeros(n_features)
    
    for i in range(n_iter):
        selected = np.random.randint(0, n_samples, batch)
        train_x = X[selected]
        train_y = y[selected]
        # print(train_x, train_y)
        # P(y=1|x) = exp_wx / (1 + exp_wx)
        # P(y=0|x) = 1 / (1 + exp_wx)
        result = _predict(train_x, w)
        update_index = (result != train_y)
        update_x = train_x[update_index]
        update_y = train_y[update_index]

        if len(update_x):
            # print(update_x.shape, update_y.shape, w.shape)
            exp_wx = np.exp(np.dot(update_x, w))
            exp_y = exp_wx / (1 + exp_wx)
            grad = np.dot(update_x.T, exp_y - update_y)
            delta = -1.0 * rate * grad / len(update_x)
            w += delta
            delta_w += delta

        if cb:
            cb(i, w, delta_w)

    return w

def _predict(X, w):
    exp_wx = np.exp(np.dot(X, w))
    return np.where(exp_wx >= 1, 1, 0)

def predict(X, w):
    X = np.hstack((X, np.ones((X.shape[0], 1))))
    return _predict(X, w)


if __name__ == '__main__':
    main()
