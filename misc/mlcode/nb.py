#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np
from collections import defaultdict

def to_cats(x, n):
    bins = np.arange(0.0, 1 + 0.1/n, 1.0 / n)
    cats = np.digitize(x, bins)
    return cats

NCATS = 10

def fit(X, y):
    (n_samples, n_features) = X.shape
    model = []

    # 统计y的分布（次数和频率）
    y_counter = defaultdict(int)
    for v in y:
        y_counter[v] += 1
    y_prob = defaultdict(float)
    for k in y_counter:
        y_prob[k] = np.log(y_counter[k] * 1.0 / n_samples)

    # 从每个特征上去分析分布
    ft_probs = []
    for ft_idx in range(n_features):
        ft = X[:, ft_idx]
        # 对该特征离散化
        cats = to_cats(ft, NCATS)
        # dist[y][x] 表示出现y,x的频数
        dist = defaultdict(lambda :defaultdict(int))
        for i in range(n_samples):
            dist[y[i]][cats[i]] += 1
        # prob[y][x] 表示出现y,x的频率
        prob = {}
        for (k, v) in list(y_counter.items()):
            d = {k2: np.log(v2 * 1.0/v) for (k2, v2) in list(dist[k].items())}
            prob[k] = d
        ft_probs.append(prob)

    model = {'y_prob': y_prob, 'ft_probs': ft_probs}
    return model

def predict(X, model):
    y_prob = model['y_prob']
    ft_probs = model['ft_probs']
    (n_samples, n_features) = X.shape

    labels = []

    # 有时候没有办法得到候选集合里面的x, y
    # 可以在这个集合上面使用一个很小的概率
    get_prob = 0
    unget_prob = 0
    eps = np.log(0.000001)

    for i in range(n_samples):
        options = []
        # 遍历所有y的可能性
        for (y, prob_base) in list(y_prob.items()):
            prob = prob_base
            cats = to_cats(X[i], NCATS)
            for ft_idx in range(n_features):
                cat = cats[ft_idx]
                if y not in ft_probs[ft_idx] or cat not in ft_probs[ft_idx][y]:
                    prob_inc = eps
                    unget_prob += 1
                else:
                    prob_inc = ft_probs[ft_idx][y][cat]
                    get_prob += 1
                prob += prob_inc
            options.append((y, prob))
        options.sort(key = lambda x: -x[1])
        label = options[0][0]
        labels.append(label)
    print('get prob = %d, unget prob = %d' % (get_prob, unget_prob))
    return np.array(labels)
