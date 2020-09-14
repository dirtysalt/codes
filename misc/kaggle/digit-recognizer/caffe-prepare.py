#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

from common import *
import h5py
from skimage.transform import rotate
from sklearn.cross_validation import train_test_split

def data_augmentation():
    start_timer()
    (data, labels) = read_train(-1)
    print_timer("read train")

    # augment data by rotating.
    data = data.reshape((-1, 1, 28, 28))
    labels = labels.reshape((-1, 1, 1, 1))
    X = data
    y = labels

    data = data.reshape((-1, 28, 28))
    for angle in (-20, -10, 10, 20):
        start_timer()
        d = np.array(map(lambda x: rotate(x, angle), data)).astype(np.float32).reshape((-1, 1, 28, 28))
        X = np.append(X, d, axis = 0)
        y = np.append(y, labels, axis = 0)
        print_timer("rotate %d" % (angle))

    tr_X, tt_X, tr_y, tt_y = train_test_split(X, y, test_size = 0.1, random_state = 42)

    start_timer()
    with h5py.File('train.hdf5','w') as f:
        max_n = tr_X.shape[0]
        xs = f.create_dataset('data', (max_n, 1, 28, 28), compression = 'gzip', dtype = np.float32)
        ys = f.create_dataset('label', (max_n, 1, 1, 1), compression = 'gzip', dtype = np.float32)
        xs[:] = tr_X
        ys[:] = tr_y
    open('train.list','w').write('train.hdf5')
    print_timer('store train')

    start_timer()
    with h5py.File('test.hdf5','w') as f:
        max_n = tt_X.shape[0]
        xs = f.create_dataset('data', (max_n, 1, 28, 28), compression = 'gzip', dtype = np.float32)
        ys = f.create_dataset('label', (max_n, 1, 1, 1), compression = 'gzip', dtype = np.float32)
        xs[:] = tt_X
        ys[:] = tt_y
    open('test.list','w').write('test.hdf5')
    print_timer('store test')

if __name__ == '__main__':
    data_augmentation()
