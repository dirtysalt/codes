#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

from common import *

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score, train_test_split
from sklearn.metrics import classification_report

import cPickle as pickle # much faster.

n = 0

# train中大部分时间花在预测10%数据上
# 如果只是简单地载入数据只花费4.38s
# 在LB分数是0.96829

RUNNING_STATS = """
load train set...
load train set: 15.77 seconds
run kNN... 
train: 196.43 seconds
load test set...
load test set: 10.38 seconds
test...
test: 1319.50 seconds
"""

def training():
    start_timer()
    print 'load train set...'
    tr = read_train(n * 2)
    (X, Y) = tr
    print_timer('load train set')

    print 'run kNN...'
    clf = KNeighborsClassifier()
    
    # # ~97% accurancy.
    # (tr_x, tt_x, tr_y, tt_y) = train_test_split(X, Y, test_size = 0.1, random_state = 0)
    # clf.fit(tr_x, tr_y)
    # y_pred = clf.predict(tt_x)
    # print classification_report(tt_y, y_pred)    
    clf.fit(X, Y)
    print_timer('train')

    # print 'dump model...'
    # # ~2G. OMG!
    # model = open('knn.model','wb')
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
    # model = open('knn.model','rb')
    # clf = pickle.load(model)
    # print_timer('load model')

    print 'test...'
    ys = clf.predict(tt)
    print_timer('test')
    write_result(ys, 'knn.csv')

if __name__ == '__main__':
    clf = training()
    testing(clf)
