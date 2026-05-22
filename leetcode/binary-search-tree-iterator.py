#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        value = top.val
        self.stack.pop()

        if top.right:
            right = top.right
            while right:
                self.stack.append(right)
                right = right.left
        return value

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
