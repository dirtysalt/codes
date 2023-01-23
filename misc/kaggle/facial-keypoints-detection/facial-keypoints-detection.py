#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import time
import cPickle
import os

# http://danielnouri.org/notes/2014/12/17/using-convolutional-neural-nets-to-detect-facial-keypoints-tutorial/

GlobalTimeStamp = 0
def start_timer():
    global GlobalTimeStamp
    GlobalTimeStamp = time.time()
def print_timer(msg):
    global GlobalTimeStamp
    _now = time.time()
    print('%s: %.2f seconds' % (msg, _now - GlobalTimeStamp))
    GlobalTimeStamp = _now

RAW = None

def read_train(cols= None):
    start_timer()
    global RAW
    if RAW is None:
        df = pd.read_csv('training.csv')
        df['Image'] = df['Image'].apply(lambda x: np.fromstring(x, sep = ' '))
        print 'cached...'
        RAW = df
    else:
        df = RAW
    if cols: df = df[list(cols) + ['Image']]
    df = df.dropna()
    print df.count()
    X = np.vstack(df['Image']) * 1.0 / 256
    y = (df[df.columns[:-1]] - 48) * 1.0 / 48
    X = X.astype(np.float32)
    y = y.astype(np.float32)
    (X, y) = shuffle(X, y, random_state = 42)
    print_timer('load training')
    return (X, y)

TEST = None

def read_test():
    start_timer()
    global TEST
    if TEST is None:
        df = pd.read_csv('test.csv')
        df['Image'] = df['Image'].apply(lambda x: np.fromstring(x, sep = ' '))
        X = np.vstack(df['Image']) * 1.0 / 256
        X = X.astype(np.float32)
        TEST = X
    else:
        X = TEST
    print_timer('load test')
    return X

def plot_loss(net1):
    import matplotlib.pyplot as pyplot
    train_loss = np.array([i["train_loss"] for i in net1.train_history_])
    valid_loss = np.array([i["valid_loss"] for i in net1.train_history_])
    pyplot.plot(train_loss, linewidth=3, label="train")
    pyplot.plot(valid_loss, linewidth=3, label="valid")
    pyplot.grid()
    pyplot.legend()
    pyplot.xlabel("epoch")
    pyplot.ylabel("loss")
    # pyplot.ylim(1e-3, 1e-2)
    pyplot.yscale("log")
    pyplot.show()

def plot_sample(x, y, axis):
    img = x.reshape(96, 96)
    axis.imshow(img, cmap='gray')
    axis.scatter(y[0::2] * 48 + 48, y[1::2] * 48 + 48, marker='x', s=10)

def plot_samples(X, y):
    import matplotlib.pyplot as pyplot
    n = X.shape[0]
    c = int(n ** 0.5)
    r = n / c
    if (n % c != 0): r += 1
    fig = pyplot.figure(figsize=(6, 6))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(n):
        ax = fig.add_subplot(r, c, i + 1, xticks=[], yticks=[])
        plot_sample(X[i], y[i], ax)
    # pyplot.savefig('samples.png')
    pyplot.show()

# 这种操作尤其需要注意in-place的问题.
def flip_op(X, y = None, flip_indices = None):
    if not flip_indices:
        flip_indices = [
        (0, 2), (1, 3),
        (4, 8), (5, 9), (6, 10), (7, 11),
        (12, 16), (13, 17), (14, 18), (15, 19),
        (22, 24), (23, 25),
        ]
    # no copy at all!
    X = X.reshape((-1, 1, 96, 96))
    X = X[:,:,:,::-1]
    if y is not None:
        y = y.copy()
        y[:,0::2] = y[:,0::2] * -1.0
        for (a, b) in flip_indices:
            y[:,(a,b)] = y[:,(b,a)]
    return (X, y)

def plot_flip(X, y):
    X0, y0 = flip_op(X, y)
    xs = []
    ys = []
    for idx in range(0, X.shape[0]):
        xs.append(X[idx])
        xs.append(X0[idx])
        ys.append(y[idx])
        ys.append(y0[idx])
    plot_samples(np.array(xs), ys)

def flip_augment(X, y, flip_indices = None):
    # no augmentation.
    if flip_indices == (): return X, y
    X = X.reshape((-1, 1, 96, 96))
    X0, y0 = flip_op(X, y, flip_indices)
    nX = np.append(X, X0, axis = 0)
    ny = np.append(y, y0, axis = 0)
    return nX, ny

INDEX_NAMES = "left_eye_center, right_eye_center, left_eye_inner_corner, left_eye_outer_corner, right_eye_inner_corner, right_eye_outer_corner, left_eyebrow_inner_end, left_eyebrow_outer_end, right_eyebrow_inner_end, right_eyebrow_outer_end, nose_tip, mouth_left_corner, mouth_right_corner, mouth_center_top_lip, mouth_center_bottom_lip".split(', ')
_names = []
INDEX_VALUES = {}
_value = 0
for _n in INDEX_NAMES:
    _names.append(_n + '_x')
    _names.append(_n + '_y')
    INDEX_VALUES[_n + '_x'] = _value
    INDEX_VALUES[_n + '_y'] = _value + 1
    _value += 2
INDEX_NAMES = _names

def write_test(ty):
    lt = pd.read_csv('IdLookupTable.csv')
    values = []
    for index, row in lt.iterrows():
        values.append((row['RowId'], ty[row.ImageId - 1][INDEX_VALUES[row.FeatureName]]))
    submission = pd.DataFrame(values, columns = ('RowId', 'Location'))
    submission.to_csv('submission.csv', index = False)

from lasagne import layers
from lasagne.updates import nesterov_momentum
from nolearn.lasagne import NeuralNet, BatchIterator
from lasagne.nonlinearities import rectify, tanh, softmax, sigmoid

# The neural net's weights are initialized from a uniform distribution with a cleverly chosen interval. That is, Lasagne figures out this interval for us, using "Glorot-style" initialization.
# http://jmlr.org/proceedings/papers/v9/glorot10a/glorot10a.pdf

# https://github.com/dnouri/nolearn/blob/master/nolearn/lasagne.py
# nolearn has wrapper of lasagne.

# !flip，validation loss = 0.002164, LB score = 3.70266
# +flip, validation loss = 0.001817, LB score = 3.59038

# 这种方式虽然灵活，但是却没有直接扩展数据集合的效果好
# ～1000 epochs, validation loss = 0.001922, 并且期间出现过许多震荡
class ANNFlipBatchIterator(BatchIterator):
    def __init__(self, batch_size = 128):
        BatchIterator.__init__(self, batch_size)

    def transform(self, X, y):
        X0, y0 = flip_augment(X, y)
        X0 = X0.reshape((-1, 96 * 96))
        return X0, y0

class EarlyStopping(object):
    def __init__(self, patience=100):
        self.patience = patience
        self.best_valid = np.inf
        self.best_valid_epoch = 0
        self.best_weights = None

    def __call__(self, nn, train_history):
        current_valid = train_history[-1]['valid_loss']
        current_epoch = train_history[-1]['epoch']
        if current_valid < self.best_valid and \
            (self.best_valid - current_valid) > 1e-6: # 不能变化过小.
            self.best_valid = current_valid
            self.best_valid_epoch = current_epoch
            self.best_weights = [w.get_value() for w in nn.get_all_params()]
        elif self.best_valid_epoch + self.patience < current_epoch:
            print("Early stopping.")
            print("Best valid loss was {:.6f} at epoch {}.".format(
                self.best_valid, self.best_valid_epoch))
            nn.load_weights_from(self.best_weights)
            raise StopIteration()

def create_net1():
    net1 = NeuralNet(
        # three layers: one hidden layer
        layers=[
        ('input', layers.InputLayer),
        ('h1', layers.DenseLayer),
        ('h2', layers.DenseLayer),
        ('output', layers.DenseLayer),
        ],

        # layer parameters:

        # variable batch size.
        input_shape=(None, 9216),  # 96x96 input pixels per batch
        h1_num_units = 400,  # number of units in hidden layer
        # 直觉上9000输入有点多，使用rectify会造成输出值幅度很大
        # 所以用tanh可以限制一下这个幅度。不过好像差别也没有那么大
        h1_nonlinearity = tanh,
        # h1_nonlinearity = rectify,

        h2_num_units = 100,
        h2_nonlinearity = rectify,

        output_nonlinearity=tanh,
        # None if output layer wants to use identity function
        output_num_units=30,  # 30 target values

        # optimization method:
        update=nesterov_momentum,
        update_learning_rate=0.02,
        update_momentum=0.9,

        regression = True,  # flag to indicate we're dealing with regression problem
        max_epochs = 2000,  # we want to train this many epochs
        eval_size = 0.1,
        # batch_iterator_train = ANNFlipBatchIterator(),
        on_epoch_finished = (EarlyStopping(5),),
        verbose=1
    )
    return net1

SPECIALIST_SETTINGS = {
    's0': # 0.002850, CNN: 0.002207
    dict(
        columns=(
            'left_eye_center_x', 'left_eye_center_y',
            'right_eye_center_x', 'right_eye_center_y',
            ),
        flip_indices=((0, 2), (1, 3)),
        ),

    's1': # 0.004231, CNN: 0.003402
    dict(
        columns=(
            'nose_tip_x', 'nose_tip_y',
            ),
        flip_indices=(),
        ),

    's2': # 0.002498, CNN: 0.001772
    dict(
        columns=(
            'mouth_left_corner_x', 'mouth_left_corner_y',
            'mouth_right_corner_x', 'mouth_right_corner_y',
            'mouth_center_top_lip_x', 'mouth_center_top_lip_y',
            ),
        flip_indices=((0, 2), (1, 3)),
        ),

    's3': # 0.005635, CNN: 0.004824
    dict(
        columns=(
            'mouth_center_bottom_lip_x',
            'mouth_center_bottom_lip_y',
            ),
        flip_indices=(),
        ),

    's4': # 0.001779, CNN: 0.001698
    dict(
        columns=(
            'left_eye_inner_corner_x', 'left_eye_inner_corner_y',
            'right_eye_inner_corner_x', 'right_eye_inner_corner_y',
            'left_eye_outer_corner_x', 'left_eye_outer_corner_y',
            'right_eye_outer_corner_x', 'right_eye_outer_corner_y',
            ),
        flip_indices=((0, 2), (1, 3), (4, 6), (5, 7)),
        ),

    's5': # 0.002209, CNN: 0.001851
    dict(
        columns=(
            'left_eyebrow_inner_end_x', 'left_eyebrow_inner_end_y',
            'right_eyebrow_inner_end_x', 'right_eyebrow_inner_end_y',
            'left_eyebrow_outer_end_x', 'left_eyebrow_outer_end_y',
            'right_eyebrow_outer_end_x', 'right_eyebrow_outer_end_y',
            ),
        flip_indices=((0, 2), (1, 3), (4, 6), (5, 7)),
        ),
    }

# ~ 0.0017
# CNN. ~ 0.001205
def train_default():
    print 'train default...'
    start_timer()
    (X, y) = read_train()
    print_timer('read train')
    X, y = flip_augment(X, y)
    if create_net is create_net1: X = X.reshape((-1, 96 * 96))
    else: X = X.reshape((-1, 1, 96, 96))
    print_timer('flip augment')
    nn = create_net()
    # nn.max_epochs = 2
    if os.path.exists('def.npy'): nn.load_weights_from('def.npy')
    nn.fit(X, y)
    print_timer('fit nn')
    ws = [w.get_value() for w in nn.get_all_params()]
    np.save('def.npy', ws)
    print_timer('dump nn')

def train_special():
    # CNN, s5不能使用def.npy训练结果，这个结果非常差
    for name in 's0 s1 s2 s3 s4 s5'.split(' '):
        settings = SPECIALIST_SETTINGS[name]
        start_timer()
        print '>>>>>train spec %s...<<<<<' % (name)
        cols = settings['columns']
        X, y = read_train(cols)
        print_timer('read train')
        flip_indices = settings['flip_indices']
        X, y = flip_augment(X, y, flip_indices)
        if create_net is create_net1: X = X.reshape((-1, 96 * 96))
        else: X = X.reshape((-1, 1, 96, 96))
        print_timer('flip augment')
        nn = create_net()
        nn.output_num_units = y.shape[1]
        # nn.max_epochs = 2
        if os.path.exists('def.npy'): nn.load_weights_from('def.npy')
        if os.path.exists('%s.npy' % (name)): nn.load_weights_from('%s.npy' % (name))
        nn.fit(X, y)
        print_timer('fit nn')
        ws = [w.get_value() for w in nn.get_all_params()]
        np.save('%s.npy' % (name), ws)
        print_timer('dump nn')

def test_default():
    tx = read_test()
    if create_net is create_net1: tx = tx.reshape((-1, 96 * 96))
    else: tx = tx.reshape((-1, 1, 96, 96))
    nn = create_net()
    nn.load_weights_from('def.npy')
    ty = nn.predict(tx)
    ty = (ty + 1) * 48.0
    # 可以限制输出范围
    # ty.clip(0, 96)
    return ty

def test_special():
    tx = read_test()
    if create_net is create_net1: tx = tx.reshape((-1, 96 * 96))
    else: tx = tx.reshape((-1, 1, 96, 96))
    specs = {}
    for name in 's0 s1 s2 s3 s4 s5'.split(' '):
        settings = SPECIALIST_SETTINGS[name]
        nn = create_net()
        nn.output_num_units = len(settings['columns'])
        nn.load_weights_from('%s.npy' % (name))
        ty = nn.predict(tx)
        ty = (ty + 1) * 48.0
        specs[name] = ty
    return specs

def test_ensemble(ty, specs):
    # keep original values.
    ty = ty.copy()
    for n in INDEX_NAMES:
        print n
        cnt = 1
        idx = INDEX_VALUES[n]
        y = ty[:,idx]
        for name in 's0 s1 s2 s3 s4 s5'.split(' '):
            settings = SPECIALIST_SETTINGS[name]
            columns = settings['columns']
            if not n in columns: continue
            idx2 = columns.index(n)
            y2 = specs[name][:,idx2]
            print y, y2
        ty[:,idx] = (y + y2) * 0.5
    return ty

# -------------------- CNN --------------------
CUDA_CONVNET = False
if CUDA_CONVNET:
    from lasagne.layers.cuda_convnet import Conv2DCCLayer, MaxPool2DCCLayer
    Conv2DLayer = Conv2DCCLayer
    MaxPool2DLayer = MaxPool2DCCLayer
else:
    Conv2DLayer = layers.Conv2DLayer
    MaxPool2DLayer = layers.MaxPool2DLayer

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

class CNNFlipBatchIterator(MiniBatchIterator):
    def __init__(self, batch_size = 128, iterations = 32):
        MiniBatchIterator.__init__(self, batch_size, iterations)

    def transform(self, X, y):
        X0, y0 = flip_augment(X, y)
        return X0, y0

import theano
def float32(k): return np.cast['float32'](k)
def Tshared(k): return theano.shared(k)

# 每次完成迭代进行权重调整. 可以让初始权重大一些，但是到后面逐渐变小
# 这样到训练后期loss可以变得更加平滑，而不是一直地震荡，这样我们可以提早结束训练
# note(dirlt): 不过感觉效果不是特别显著，因为训练后期weight-delta也在不断变小.
# note(dirlt @ 2015-04-17): 在GPU上跑确实发现了这个问题，在后期不断地有震荡出现，从0.0018 -> 0.002 -> 0.0018
class EpochFinishedCallback:
    def __init__(self, lr_start, lr_stop):
        self.lr_start = lr_start
        self.lr_stop = lr_stop
        self.lr_values = None

    def __call__(self, nn, tr_hist):
        if self.lr_values is None:
            self.lr_values = np.linspace(self.lr_start, self.lr_stop, nn.max_epochs) # 线性插值
        current_epoch = tr_hist[-1]['epoch']
        lr_value = float32(self.lr_values[current_epoch - 1])
        nn.update_learning_rate = lr_value

# 不要一上来就开始加dropout. 这样会降低训练速度。只有确定出现overfitting情况的时候再开始添加
# training和validation error差别很大的时候，可以认为出现overfitting. 首先想到的是应该增加数据，然后考虑regularization(weight-decay or dropout).
# 直到overfitting现象消失，然后再考虑增加模型复杂度来增加精确度，之后继续出现overfitting，这样不断迭代改进。

# note(dirlt @ 2015-04-17): 借用同事GPU搞了一把. 效果确实不错ANN = 3.08932, CNN = 2.67626
def create_net2():
    net2 = NeuralNet(
        # three layers: one hidden layer
        layers=[
        ('input', layers.InputLayer),

        ('conv1', Conv2DLayer),
        ('pool1', MaxPool2DLayer),
        # ('dropout1', layers.DropoutLayer),

        ('conv2', Conv2DLayer),
        ('pool2', MaxPool2DLayer),
        # ('dropout2', layers.DropoutLayer),

        ('hidden3', layers.DenseLayer),
        # ('dropout3', layers.DropoutLayer),

        ('output', layers.DenseLayer),
        ],

        # layer parameters:

        # variable batch size.
        input_shape=(None, 1, 96, 96),  # 96x96 input pixels per batch

        conv1_num_filters = 32, conv1_filter_size = (3, 3), pool1_ds = (2, 2),
        # dropout1_p = 0.5,
        conv1_nonlinearity = rectify,
        conv2_num_filters = 64, conv2_filter_size=(3, 3), pool2_ds=(2, 2),
        # dropout2_p = 0.5,
        conv2_nonlinearity = rectify,

        hidden3_num_units=300,  # number of units in hidden layer
        # dropout3_p = 0.25,
        hidden3_nonlinearity=rectify,

        output_nonlinearity=tanh,  # output layer uses identity function
        output_num_units=30,  # 30 target values

        # optimization method:
        update=nesterov_momentum,
        update_learning_rate=Tshared(float32(0.02)),
        update_momentum=Tshared(float32(0.9)),

        regression = True,  # flag to indicate we're dealing with regression problem
        max_epochs = 400,  # we want to train this many epochs
        eval_size = 0.1,
        # batch_iterator_train = CNNFlipBatchIterator(batch_size = 128, iterations = 16),
        on_epoch_finished = (EarlyStopping(5),),
        # on_epoch_finished = [ # could have multiple callbacks.
        #         EpochFinishedCallback(0.02, 0.005),
        #     ],
        verbose=1,
    )
    return net2

# create_net = create_net1
create_net = create_net2
