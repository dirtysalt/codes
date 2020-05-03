#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

from common import *

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn.metrics import classification_report

import cPickle as pickle # much faster.

n = 0

# 运行时间比kNN快不少. 下面是 n = 1000 的情况
# 因为运行时间少，所以我可以用全量数据重新计算模型
# oob_score = 0.96857 , LB score = 0.96757

RUNNING_STATS = """
load train set...
load train set: 14.78 seconds
train: 224.33 seconds
dump model...
dump model: 287.68 seconds
load test set...
load test set: 14.81 seconds
test...
test: 9.08 seconds
"""

def training():
    start_timer()
    print 'load train set...'
    tr = read_train(n * 2)
    (X, Y) = tr
    print_timer('load train set')

    print 'run rf...'
    clf = RandomForestClassifier(n_estimators = 1000, oob_score = True)

    # # ~97% accurancy.
    # (tr_x, tt_x, tr_y, tt_y) = train_test_split(X, Y, test_size = 0.1, random_state = 0)
    # clf.fit(tr_x, tr_y)
    # y_pred = clf.predict(tt_x)
    # print classification_report(tt_y, y_pred)
    clf.fit(X, Y)
    print clf.oob_score_
    print_timer('train')
    
    # print 'dump model...'
    # ~3.6G
    # model = open('rf.model','wb')
    # pickle.dump(clf, model)
    # model.close()
    # print_timer('dump model')

    return clf

def testing(clf):
    start_timer()
    print 'load test set...'
    tt = read_test(n)
    print_timer('load test set')

    # print 'load model...'
    # model = open('rf.model','rb')
    # clf = pickle.load(model)
    # print_timer('load model')

    print 'test...'
    ys = clf.predict(tt)
    print_timer('test')
    write_result(ys, 'rf.csv')

if __name__ == '__main__':
    clf = training()
    testing(clf)
