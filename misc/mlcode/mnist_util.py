#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pickle

import cv2
import numpy as np
import pandas as pd


def load_train_data():
    train_data = pd.read_csv('/Users/dirlt/Downloads/lihang_book_algorithm-master/data/train.csv')
    return train_data


def load_test_data():
    test_data = pd.read_csv('/Users/dirlt/Downloads/lihang_book_algorithm-master/data/test.csv')
    return test_data


def get_image_data(data):
    fields = list([x for x in data.columns if x.startswith('pixel')])
    pixels = data[fields].values
    return pixels


def get_target_data(data):
    return data['label'].values


def _image_data_to_hog_feature(hog, data):
    img = np.reshape(data, (28, 28))
    cv_img = img.astype(np.uint8)
    hog_feature = hog.compute(cv_img)
    return hog_feature


def image_data_to_hog_feature(data):
    hog = cv2.HOGDescriptor('hog.xml')
    outputs = []
    for x in data:
        features = _image_data_to_hog_feature(hog, x)
        outputs.append(features)
    outputs = np.array(outputs).reshape((-1, 324))
    return outputs


def save_to_pickle():
    train_data = load_train_data()
    X = image_data_to_hog_feature(get_image_data(train_data))
    Y = get_target_data(train_data)
    mnist_data = {'X': X, 'Y': Y}
    pickle.dump(mnist_data, open('mnist_data.pkl', 'wb'))


def load_from_pickle():
    mnist_data = pickle.load(open('mnist_data.pkl', 'rb'))
    X = mnist_data['X']
    Y = mnist_data['Y']
    return X, Y


def train_test_split(X, Y):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    return X_train, X_test, y_train, y_test
