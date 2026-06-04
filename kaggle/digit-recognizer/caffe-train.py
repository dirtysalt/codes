#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import sys
import os
sys.path.append(os.path.join(os.environ['HOME'], 'repo/caffe/python'))
import caffe
import numpy as np
from sklearn.cross_validation import train_test_split
from common import *
import h5py

# start_timer()
# f = h5py.File('train.hdf5')
# tr_x = f['data'].value
# tr_y = f['label'].value
# f.close()
# print_timer('read train')

# f = h5py.File('test.hdf5')
# tt_x = f['data'].value
# tt_y = f['label'].value
# print_timer('read test')

solver = caffe.get_solver('caffe-conf/solver.prototxt')
# solver.restore('uv_iter_5000.solverstate')

start_timer()
# solver.net.set_input_arrays(tr_x, tr_y)
# solver.test_nets[0].set_input_arrays(tt_x, tt_y)
solver.solve()
print_timer("solve")
