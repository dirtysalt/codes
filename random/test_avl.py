#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1
        self.weight = value

    @staticmethod
    def height(r):
        return r.height if r else 0

    @staticmethod
    def size(r):
        return r.size if r else 0

    @staticmethod
    def weight(r):
        return r.weight if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(Tree.height(root.left), Tree.height(root.right)) + 1
    root.size -= Tree.size(left.left) + 1
    root.weight -= Tree.weight(left.left) + left.value

    left.right = root
    left.height = max(Tree.height(left.left), Tree.height(left.right)) + 1
    left.size += Tree.size(root.right) + 1
    left.weight += Tree.weight(root.right) + root.value
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(Tree.height(root.left), Tree.height(root.right)) + 1
    root.size -= Tree.size(right.right) + 1
    root.weight -= Tree.weight(right.right) + right.value

    right.left = root
    right.height = max(Tree.height(right.left), Tree.height(right.right)) + 1
    right.size += Tree.size(root.left) + 1
    right.weight += Tree.weight(root.left) + root.value
    return right


def do_balance(root):
    lh = Tree.height(root.left)
    rh = Tree.height(root.right)

    if (lh - rh) >= 2:
        llh = Tree.height(root.left.left)
        lrh = Tree.height(root.left.right)
        if lrh > llh:
            root.left = right_rotate(root.left)
        root = left_rotate(root)

    elif (rh - lh) >= 2:
        rlh = Tree.height(root.right.left)
        rrh = Tree.height(root.right.right)
        if rlh > rrh:
            root.right = left_rotate(root.right)
        root = right_rotate(root)

    else:
        root.height = max(lh, rh) + 1

    return root
