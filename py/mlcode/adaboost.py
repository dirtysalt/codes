#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import decision_tree as dt
import numpy as np

class WeakClassifier(object):
    def __init__(self):
        pass

    def fit(self, X, y, dist, max_depth):
        tree = dt.fit(X, y, dist, max_depth)
        self.tree = tree

    def predict(self, X):
        y = dt.predict(X, self.tree)
        return y

class AdaBoost(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.dist = None
        self.models = []

    def _fit(self, X, y, dist):
        clf = WeakClassifier()
        clf.fit(X, y, dist, max_depth = 2)
        y_pred = clf.predict(X)
        # assert((sum(y_pred == 1)  + sum(y_pred == -1)) == len(y_pred))
        error_rate = np.sum(np.where((y_pred == y), 0, 1) * (dist / np.sum(dist)))
        print('error rate = %.4f' % error_rate)
        clf_weight = 0.5 * np.log((1.0 - error_rate) / error_rate)
        expv = np.exp(-1.0 * clf_weight * y_pred * y)
        expvw = expv * dist
        new_dist = expvw / np.sum(expvw)
        return new_dist, error_rate, clf, clf_weight

    def fit(self, X, y, n_iter = 10):
        y = np.where(y == 1, 1, -1)
        n_samples, n_features = X.shape
        dist = self.dist
        if dist is None:
            dist = np.ones(n_samples)
        for i in range(n_iter):
            print('training weak clf #%d' % i)
            new_dist, error_rate, clf, clf_weight = self._fit(X, y, dist)
            # note(yan): 这个地方如果是0.5的话说明问题还蛮大的.
            if error_rate == 0.5:
                break
            dist = new_dist
            self.models.append((clf, clf_weight))
            print('done. weight = %.4f' % self.models[-1][1])
        self.dist = dist

    def predict(self, X):
        n_samples, _ = X.shape
        values = np.zeros(n_samples)
        for m in self.models:
            v = m[0].predict(X) * m[1]
            values += v
        labels = np.where(values > 0, 1, 0)
        return labels
