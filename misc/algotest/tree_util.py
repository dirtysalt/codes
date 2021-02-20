#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import os
import random


def tree_to_dot(t, name, stream):
    id_name = name.replace(' ', '').replace('-', '_')

    def setNN(t):
        t._node_name = 'nn_{}_{}'.format(id_name, random.randint(0, 1000000))

    class NilNode:
        def __init__(self):
            self.left = self.right = None
            setNN(self)

        def data(self):
            return "nil"

    def P(*objects, **kwargs):
        print(*objects, file=stream, **kwargs)

    def NN(t):
        return t._node_name

    def resetNN(t):
        if t is None:
            return

        setNN(t)
        if t.left is not None:
            resetNN(t.left)

        if t.right is not None:
            resetNN(t.right)

    resetNN(t)

    nodes = []

    def fn(level, t):
        if t is None:
            return
        nodes.append(t)
        if t.left is None and t.right is None:
            return

        if t.left:
            P('{} -- {}'.format(NN(t), NN(t.left)))
            fn(level + 1, t.left)
        else:
            x = NilNode()
            nodes.append(x)
            P('{} -- {}'.format(NN(t), NN(x)))

        if t.right:
            P('{} -- {}'.format(NN(t), NN(t.right)))
            fn(level + 1, t.right)
        else:
            x = NilNode()
            nodes.append(x)
            P('{} -- {}'.format(NN(t), NN(x)))

    P('graph %s {' % (id_name))
    P('rankdir="TB"')
    P('label="{}"'.format(name))
    fn(1, t)
    for t in nodes:
        P('{} [label="{}"]'.format(NN(t), t.data()))
    P('}')


def dot_to_graph(name, text, type='png'):
    dot_name = name + '.dot'
    graph_name = name + '.' + type

    with open(dot_name, 'w') as fh:
        fh.write(text)

    os.system('gvpack -u {} | dot -T{} -o {}'.format(dot_name, type, graph_name))
    return graph_name
