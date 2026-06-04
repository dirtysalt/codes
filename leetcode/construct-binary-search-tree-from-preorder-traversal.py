#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def cons(p):
            if not p:
                return None
            i = 1
            while i < len(p):
                if p[i] > p[0]:
                    break
                i += 1
            left = cons(p[1:i])
            right = cons(p[i:])
            t = TreeNode(p[0])
            t.left = left
            t.right = right
            return t

        root = cons(preorder)
        return root
