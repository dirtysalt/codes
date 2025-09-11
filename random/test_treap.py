#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random
from io import StringIO

from tree_util import dot_to_graph, tree_to_dot


class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = self.right = None
        self.priority = random.randint(0, 100)

    def data(self):
        return "{}-{}".format(self.val, self.priority)


def left_rotate(r: TreeNode, rl: TreeNode):
    if r.priority <= rl.priority:
        return r

    r.left = rl.right
    rl.right = r
    return rl


def right_rotate(r: TreeNode, rr: TreeNode):
    if r.priority <= rr.priority:
        return r

    r.right = rr.left
    rr.left = r
    return rr


def insert_tree_node(root: TreeNode, t: TreeNode):
    if root is None:
        return t

    if t.val < root.val:
        root.left = insert_tree_node(root.left, t)
        root = left_rotate(root, root.left)
    elif t.val > root.val:
        root.right = insert_tree_node(root.right, t)
        root = right_rotate(root, root.right)
    else:
        pass

    return root


def delete_tree_node(root: TreeNode, val):
    if root is None:
        return None

    if val < root.val:
        root.left = delete_tree_node(root.left, val)
        return root
    elif val > root.val:
        root.right = delete_tree_node(root.right, val)
        return root

    root.priority = 1 << 30  # mark this node priority as high enough
    if root.left and ((root.right is None) or (root.left.priority < root.right.priority)):
        root = left_rotate(root, root.left)
        root.right = delete_tree_node(root.right, val)

    elif root.right and ((root.left is None) or (root.left.priority >= root.right.priority)):
        root = right_rotate(root, root.right)
        root.left = delete_tree_node(root.left, val)

    else:  # left and right are None
        assert root.left is None and root.right is None
        return None

    return root


def test_pprint_tree():
    root = None
    stream = StringIO()

    random.seed(23)

    N = 12
    for val in range(N, 0, -1):
        root = insert_tree_node(root, TreeNode(val))
        # tree_to_dot(root, 'ins {}'.format(val), stream)
    tree_to_dot(root, 'now', stream)

    delete_tree_node(root, 1)
    tree_to_dot(root, 'delete 1', stream)

    delete_tree_node(root, 2)
    tree_to_dot(root, 'delete 2', stream)

    dot_to_graph('/tmp/example', stream.getvalue(), type='png')


test_pprint_tree()
