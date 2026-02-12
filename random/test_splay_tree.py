#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from math import log2

import random
from io import StringIO

from tree_util import dot_to_graph, tree_to_dot


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = self.right = None

    def data(self):
        return self.val


def insert_tree_node(root: TreeNode, t: TreeNode):
    if root is None:
        return t

    saved = root

    while root:
        p = root
        if t.val > root.val:
            root = root.right
        else:
            root = root.left

    if t.val > p.val:
        assert p.right is None
        p.right = t
    else:
        assert p.left is None
        p.left = t

    return saved


def uplift_left(r, rl):
    r.left = rl.right
    rl.right = r
    return rl


def uplift_right(r, rr):
    r.right = rr.left
    rr.left = r
    return rr


def left_zig_zig(r, rl, rll):
    rl.left = rll.right
    r.left = rl.right
    rl.right = r
    rll.right = rl
    return rll


def left_zig_zag(r, rl, rll):
    rl.right = rll.left
    r.left = rll.right
    rll.left = rl
    rll.right = r
    return rll


def right_zig_zig(r, rr, rrr):
    rr.right = rrr.left
    r.right = rr.left
    rr.left = r
    rrr.left = rr
    return rrr


def right_zig_zag(r, rr, rrl):
    r.right = rrl.left
    rr.left = rrl.right
    rrl.left = r
    rrl.right = rr
    return rrl


def find_depth_of_value(r: TreeNode, val):
    depth = 1
    while r and r.val != val:
        depth += 1
        if val < r.val:
            r = r.left
        else:
            r = r.right
    return depth


def find_tree_node(r: TreeNode, val):
    if r is None or r.val == val:
        return r

    if val < r.val:
        rl = r.left

        if rl is None:
            return r

        elif val == rl.val:
            return uplift_left(r, rl)

        elif val < rl.val:
            rll = rl.left
            if rll is None:
                return uplift_left(r, rl)
            else:
                rll = rl.left = find_tree_node(rll, val)
                return left_zig_zig(r, rl, rll)

        else:
            rlr = rl.right
            if rlr is None:
                return uplift_left(r, rl)
            else:
                rlr = rl.right = find_tree_node(rlr, val)
                return left_zig_zag(r, rl, rlr)

    else:
        rr = r.right
        if rr is None:
            return r

        elif val == rr.val:
            return uplift_right(r, rr)

        elif val < rr.val:
            rrl = rr.left
            if rrl is None:
                return uplift_right(r, rr)
            else:
                rrl = rr.left = find_tree_node(rrl, val)
                return right_zig_zag(r, rr, rrl)

        else:
            rrr = rr.right
            if rrr is None:
                return uplift_right(r, rr)
            else:
                rrr = rr.right = find_tree_node(rrr, val)
                return right_zig_zig(r, rr, rrr)

    raise RuntimeError('unexpected condition')


def test_pprint_tree():
    root = None
    stream = StringIO()
    N = 32
    for val in range(N, 0, -1):
        # print('insert value {}'.format(val))
        root = insert_tree_node(root, TreeNode(val))
        # tree_to_dot(root, 'ins {}'.format(val), stream)

    for x in (1, 2, 1, 2, 3, 4):
        root = find_tree_node(root, x)
        tree_to_dot(root, 'find {}'.format(x), stream)
    dot_to_graph('/tmp/example', stream.getvalue(), type='png')


test_pprint_tree()


def test_always_on_top():
    root = None
    N = 128
    for val in range(N, 0, -1):
        root = insert_tree_node(root, TreeNode(val))

    for x in range(1, N + 1):
        root = find_tree_node(root, x)
        depth = find_depth_of_value(root, x)
        assert depth == 1


# test_always_on_top()

def do_benchmark():
    root = None
    n_nodes, n_queries, ratio = 1024, 10000, 0.9
    # assume 1 will draw 'n_queries' times
    # and 2 will be draw 'n_queries' * 0.9 times
    # and so on. and shuffle them.
    queries = []
    count = n_queries
    for i in range(1, n_nodes + 1):
        queries.extend([i] * count)
        count = int(count * ratio)
    print('# of total queries = {}'.format(len(queries)))
    random.shuffle(queries)

    print('# of tree nodes = {}'.format(n_nodes))
    for x in range(n_nodes, 0, -1):
        root = insert_tree_node(root, TreeNode(x))

    depth_sum = 0
    for q in queries:
        depth = find_depth_of_value(root, q)
        depth_sum += depth
        root = find_tree_node(root, q)
        assert root.val == q

    print('depth sum of queries = {}, avg depth = {}'.format(depth_sum, depth_sum / len(queries)))
    print('M * logN = {} * {} = {}'.format(n_queries, n_nodes, n_queries * log2(n_nodes)))

# do_benchmark()
