#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


def fit(X, y):
    np.random.seed(42)
    X = np.hstack((X, np.ones((X.shape[0], 1))))
    y = np.where(y == 1, 1, -1)
    print('X.shape = %s, y.shape = %s' % (X.shape, y.shape))

    (n_samples, n_features) = X.shape
    # w = np.zeros(n_features)
    w = np.random.randn(n_features)
    # print(w)

    batch = 100
    n_iter = 10000
    rate = 0.5

    for i in range(n_iter):
        selected = np.random.randint(0, n_samples, batch)
        train_x = X[selected]
        train_y = y[selected]
        # print(train_x, train_y)
        result = train_y * np.dot(train_x, w)
        update_index = (result <= 0)
        update_x = train_x[update_index]
        update_y = train_y[update_index]

        if len(update_x):
            grad = np.dot(update_x.T, update_y)
            delta = rate * grad / len(update_x)
            w += delta

    return w


def predict(X, w):
    X = np.hstack((X, np.ones((X.shape[0], 1))))
    y = np.dot(X, w)
    return np.where(y > 0, 1, 0)


if __name__ == '__main__':
    main()
