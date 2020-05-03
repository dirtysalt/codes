#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def height(r):
    return r.height if r else 0


def left_rotate(root):
    # print('left_rotate!')
    left = root.left
    root.left = left.right
    root.height = max(height(root.left), height(root.right)) + 1

    left.right = root
    left.height = max(height(left.left), height(left.right)) + 1
    return left


def right_rotate(root):
    # print('right_rotate!')
    right = root.right
    root.right = right.left
    root.height = max(height(root.left), height(root.right)) + 1

    right.left = root
    right.height = max(height(right.left), height(right.right)) + 1
    return right


def balance(root):
    lh = height(root.left)
    rh = height(root.right)

    if (lh - rh) >= 2:
        llh = height(root.left.left)
        lrh = height(root.left.right)
        if lrh > llh:
            root.left = right_rotate(root.left)
        root = left_rotate(root)

    elif (rh - lh) >= 2:
        rlh = height(root.right.left)
        rrh = height(root.right.right)
        if rlh > rrh:
            root.right = left_rotate(root.right)
        root = right_rotate(root)

    else:
        root.height = max(lh, rh) + 1

    return root
