#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        pp = {}
        nodes = {}

        for p, c, isLeft in descriptions:
            if p not in nodes:
                t = TreeNode(p)
                nodes[p] = t
                pp[p] = -1

            if c not in nodes:
                t = TreeNode(c)
                nodes[c] = t
                pp[c] = -1

            if isLeft:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            pp[c] = p

        for x, y in pp.items():
            if y == -1:
                return nodes[x]


if __name__ == '__main__':
    pass
