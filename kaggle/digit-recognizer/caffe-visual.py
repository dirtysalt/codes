#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import os
import sys
sys.path.append(os.path.join(os.environ['HOME'], 'repo/caffe/python'))
import caffe

import caffe.draw
from caffe.proto import caffe_pb2
from google.protobuf import text_format

caffe.set_mode_cpu()
net = caffe.Net('caffe-conf/test.prototxt',
                'uv_iter_9500.caffemodel',
                caffe.TEST)

from common import *
data = read_test(10)
start_timer()
data = data.reshape((-1, 1, 28, 28))
out = net.forward_all(**{'data': data})
blobs = net._blobs
idx = 1
for name in net._layer_names: print 'layer#%d = %s' %(idx, name); idx += 1

import pylab as plt
import matplotlib.cm as cm

def simple_plot(data, r0, c0, fname):
    fig, axs = plt.subplots(r0, c0)
    for r in range(0, r0):
        for c in range(0, c0):
            ax = axs[r][c]
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            im = data[r * c0 + c]
            ax.imshow(im, cmap = cm.Greys_r)
    if fname: plt.savefig(fname, dpi = 72)
    else: plt.show()

nth = 2 # nth instance
print 'conv1...'
data = blobs[1].data[nth] # conv1
simple_plot(data, 4, 8, 'caffe-conv1.png')

print 'pool1...'
data = blobs[2].data[nth] # pool1
simple_plot(data, 4, 8, 'caffe-pool1.png')

print 'conv2...'
data = blobs[5].data[nth] # conv2
simple_plot(data, 8, 8, 'caffe-conv2.png')

print 'pool2...'
data = blobs[6].data[nth] # pool2
simple_plot(data, 8, 8, 'caffe-pool2.png')
