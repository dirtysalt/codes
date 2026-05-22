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

print 'train...'
net = caffe_pb2.NetParameter()
text_format.Merge(open('caffe-conf/train.prototxt').read(), net)
caffe.draw.draw_net_to_file(net, 'caffe-train.png', 'LR')

print 'test...'
net = caffe_pb2.NetParameter()
text_format.Merge(open('caffe-conf/test.prototxt').read(), net)
caffe.draw.draw_net_to_file(net, 'caffe-test.png', 'LR')
