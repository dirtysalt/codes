#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np
from collections import Counter

def calc_ent(x, dist):
    """
        calculate shanno ent of x
    """

    assert(len(x) == len(dist))
    x_value_list = set([x[i] for i in range(x.shape[0])])
    dist_sum = np.sum(dist)
    ent = 0.0
    for x_value in x_value_list:
        index = (x == x_value)
        sub_dist = dist[index]
        sub_dist_sum = np.sum(sub_dist)
        p = sub_dist_sum / dist_sum
        logp = np.log2(p)
        ent -= p * logp

    return ent

def calc_condition_ent(x, y, dist):
    """
        calculate ent H(y|x)
    """

    # calc ent(y|x)
    assert(len(x) == len(dist) == len(y))
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    dist_sum = np.sum(dist)
    for x_value in x_value_list:
        index = (x == x_value)
        sub_y = y[index]
        sub_dist = dist[index]
        temp_ent = calc_ent(sub_y, sub_dist)
        sub_dist_sum = np.sum(sub_dist)
        ent += sub_dist_sum * temp_ent / dist_sum

    return ent

def calc_ent_gap(x, y, dist):
    """
        calculate ent gap
    """

    base_ent = calc_ent(y, dist)
    condition_ent = calc_condition_ent(x, y, dist)
    ent_gap = base_ent - condition_ent

    return ent_gap

class Node(object):
    def __init__(self, ft_index, default_label):
        self.ft_index = ft_index
        self.default_label = default_label
        self.nodes = {}

    def append(self, ft_bound, node):
        # self.ft_bounds.append(ft_bound)
        # self.nodes.append(node)
        self.nodes[ft_bound] = node


def make_tree(X, y, feature_indexs, dist, max_depth):
    label_counter = Counter(y)
    default_label = label_counter.most_common()[0][0]
    if len(label_counter) == 1 or \
      len(feature_indexs) <= 0 or \
      len(y) <= 20 or \
      max_depth == 0:
        return Node(None, default_label)

    max_ent_gap = -1000000000
    max_ft_idx = None
    for ft_idx in feature_indexs:
        ent_gap = calc_ent_gap(X[:, ft_idx], y, dist)
        if ent_gap > max_ent_gap:
            max_ent_gap = ent_gap
            max_ft_idx = ft_idx

    if max_ent_gap < 0.1:
        return Node(None, default_label)

    node = Node(max_ft_idx, default_label)
    next_feature_indexs = feature_indexs[:]
    next_feature_indexs.remove(max_ft_idx)

    values = set(X[:, max_ft_idx])
    for v in values:
        sub_index = (X[:, max_ft_idx] == v)
        sub_x = X[sub_index]
        sub_y = y[sub_index]
        sub_dist = dist[sub_index]
        if len(sub_y) == 0:
            continue
        sub_node = make_tree(sub_x, sub_y, next_feature_indexs, sub_dist, max_depth - 1)
        node.append(v, sub_node)

    # print('select ft#%d / %d. max entropy gap = %.2f' % (max_ft_idx, len(feature_indexs), max_ent_gap))
    return node

def fit(X, y, dist = None, max_depth = None):
    n_samples, n_features = X.shape
    if dist is None:
        dist = np.ones(n_samples)
    if max_depth is None:
        max_depth = 10000
    tree = make_tree(X, y, list(range(n_features)), dist, max_depth)
    return tree

def predict(X, root):
    labels = []
    for i in range(X.shape[0]):
        tree = root
        while True:
            ft_index = tree.ft_index
            label = tree.default_label
            if ft_index is None:
                break
            v = X[i, ft_index]
            if v not in tree.nodes:
                # print('not in tree nodes. use default label')
                break
            tree = tree.nodes[v]
        labels.append(label)
    return np.array(labels)

def tree_to_dict(tree):
    d = {}
    if tree.ft_index  is not None:
        d['ft_index'] = tree.ft_index
    d['label'] = tree.default_label
    for (v, node) in list(tree.nodes.items()):
        d['ft_value_%s' % v] = tree_to_dict(node)
    return d

def print_tree(tree, output_file):
    import pprint
    d = tree_to_dict(tree)
    with open(output_file, 'w') as fh:
        pprint.pprint(d, stream = fh)
