#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import pandas as pd
from sklearn.cross_validation import train_test_split
from nolearn.lasagne import NeuralNet, BatchIterator
from lasagne import layers
from lasagne.nonlinearities import softmax, rectify, tanh
from lasagne.updates import momentum, nesterov_momentum, sgd, rmsprop
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle
# import h5py
from nolearn.lasagne import BatchIterator

def plot_loss(net):
    from matplotlib import pyplot
    """
    Plot the training loss and validation loss versus epoch iterations with respect to
    a trained neural network.
    """
    train_loss = np.array([i["train_loss"] for i in net.train_history_])
    valid_loss = np.array([i["valid_loss"] for i in net.train_history_])
    pyplot.plot(train_loss, linewidth = 3, label = "train")
    pyplot.plot(valid_loss, linewidth = 3, label = "valid")
    pyplot.grid()
    pyplot.legend()
    pyplot.xlabel("epoch")
    pyplot.ylabel("loss")
    #pyplot.ylim(1e-3, 1e-2)
    pyplot.yscale("log")
    pyplot.show()

RAW = None

def read_train():
    global RAW
    if RAW: return RAW
    train_df = pd.read_csv('./train.csv')
    train_label = train_df.values[:, 0]
    train_data = train_df.values[:, 1:] * 1.0 / 256
    (X, y) = (train_data.astype(np.float32), train_label.astype(np.int32))
    (X, y) = shuffle(X, y, random_state = 42)
    RAW = (X, y)
    return (X, y)

# def read_train2():
#     # see caffe-prepare.py
#     f = h5py.File('train.hdf5')
#     data = f['data'].value.astype(np.float32)
#     labels = f['label'].value.astype(np.int32)
#     (X, y) = shuffle(data, labels, random_state = 42)
#     return (X, y)

TEST = None
def read_test():
    global TEST
    if TEST: return TEST
    test_df = pd.read_csv('./test.csv')
    X = test_df.values.astype(np.float32) * 1.0 / 256
    TEST = X
    return X

CUDA_CONVNET = False
if CUDA_CONVNET:
    from lasagne.layers.cuda_convnet import Conv2DCCLayer, MaxPool2DCCLayer
    Conv2DLayer = Conv2DCCLayer
    MaxPool2DLayer = MaxPool2DCCLayer
else:
    Conv2DLayer = layers.Conv2DLayer
    MaxPool2DLayer = layers.MaxPool2DLayer

def create_ann():
    nn = NeuralNet(
    layers = [  # three layers: one hidden layer
        ('input', layers.InputLayer),
        ('h1', layers.DenseLayer),
        ('d1', layers.DropoutLayer),
        ('h2', layers.DenseLayer),
        ('d2', layers.DropoutLayer),
        ('output', layers.DenseLayer),
        ],
    # layer parameters:
    input_shape = (None, 784),  # 28x28 input pixels per batch
    h1_num_units = 400,  # number of units in hidden layer
    h1_nonlinearity = tanh,
    d1_p = 0.25,
    h2_num_units = 100,
    h2_nonlinearity = rectify,
    d2_p = 0.25,
    output_nonlinearity = softmax,  # output layer uses softmax function
    output_num_units = 10,  # 10 labels

    # optimization method:
    update = nesterov_momentum,
    update_learning_rate = 0.01,
    update_momentum = 0.9,

    eval_size = 0.1,
    max_epochs = 100,
    verbose = 1,
    )
    return nn

class MiniBatchIterator(BatchIterator):
    def __init__(self, batch_size = 128, iterations = 32):
        BatchIterator.__init__(self, batch_size)
        self.iterations = iterations
        self.X = None
        self.y = None
        self.cidx = 0
        self.midx = 0

    def __call__(self, X, y = None):
        # reset data set.
        if not (self.X is X and self.y is y):
            self.cidx = 0
            n_samples = X.shape[0]
            bs = self.batch_size
            self.midx = (n_samples + bs - 1) // bs
        self.X, self.y = X, y
        return self

    def __iter__(self):
        bs = self.batch_size
        for i in range(0, self.iterations):
            sl = slice(self.cidx * bs , (self.cidx + 1) * bs)
            self.cidx += 1
            # wrap up.
            if self.cidx >= self.midx: self.cidx = 0
            Xb = self.X[sl]
            if self.y is not None:
                yb = self.y[sl]
            else:
                yb = None
            yield self.transform(Xb, yb)

from skimage.transform import rotate
class CNNRotateBatchIterator(BatchIterator):
    def __init__(self, batch_size = 128, iterations = 32):
        BatchIterator.__init__(self, batch_size)

    def transform(self, X, y):
        n = X.shape[0]
        angles = np.random.uniform(-16, 16, n)
        x2 = zip(X.reshape((-1, 28, 28)), angles)
        x3 = np.array(map(lambda x: rotate(x[0], x[1]), x2))
        x3 = x3.astype(np.float32).reshape((-1, 1, 28, 28))
        return x3, y

def create_cnn():
    nn = NeuralNet(
    layers = [  # three layers: one hidden layer
        ('input', layers.InputLayer),

        ('conv1', Conv2DLayer),
        ('pool1', MaxPool2DLayer),
        ('dropout1', layers.DropoutLayer),

        ('conv2', Conv2DLayer),
        ('pool2', MaxPool2DLayer),
        ('dropout2', layers.DropoutLayer),

        # ('conv3', Conv2DLayer),
        # ('pool3', MaxPool2DLayer),
        # ('dropout3', layers.DropoutLayer),

        ('hidden4', layers.DenseLayer),
        ('dropout4', layers.DropoutLayer),

        ('output', layers.DenseLayer),
        ],
    # layer parameters:
    input_shape = (None, 1, 28, 28),  # 28x28 input pixels per batch

    conv1_num_filters = 32, conv1_filter_size = (3, 3), pool1_ds = (2, 2),
    conv1_nonlinearity = rectify,
    dropout1_p = 0.5,

    conv2_num_filters = 64, conv2_filter_size=(3, 3), pool2_ds=(2, 2),
    conv2_nonlinearity = rectify,
    dropout2_p = 0.5,

    # conv3_num_filters = 128, conv3_filter_size = (2, 2), pool3_ds = (2, 2),
    # conv3_nonlinearity = rectify,
    # dropout3_p = 0.5,

    hidden4_num_units = 500,
    hidden4_nonlinearity = rectify,
    # hidden4_nonlinearity = tanh,
    dropout4_p = 0.5,

    output_num_units = 10,  # 10 labels
    output_nonlinearity = softmax,  # output layer uses softmax function

    # optimization method:
    update = nesterov_momentum,
    update_learning_rate = 0.01,
    update_momentum = 0.9,

    eval_size = 0.1,

    max_epochs = 200,  # we want to train this many epochs
    verbose = 1,
    batch_iterator_train = CNNRotateBatchIterator(batch_size = 128, iterations = 4)
    )
    return nn

def write_test(pred):
    output = pd.DataFrame(data = {"ImageId": range(1, 28001), "Label": pred})
    output.to_csv("./cnn.csv", index = False, quoting = 3)
