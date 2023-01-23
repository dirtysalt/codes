#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import os
import sys
sys.path.append(os.path.join(os.environ['HOME'], 'repo/caffe/python'))
import caffe

caffe.set_mode_cpu()
net = caffe.Net('caffe-conf/test.prototxt',
                'uv_iter_10000.caffemodel',
                caffe.TEST)

from common import *
data = read_test(-1)
start_timer()
data = data.reshape((-1, 1, 28, 28))
out = net.forward_all(**{'data': data})
rs = out['prob']
print_timer("predict")
ys = map(lambda x: find_max_idx(x), rs)
write_result(ys, 'caffe.csv')
