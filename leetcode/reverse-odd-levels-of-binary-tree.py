#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        before = [root]

        depth = 0
        while True:
            next = []
            for x in before:
                next.append(x.left)
                next.append(x.right)
            next = [x for x in next if x is not None]
            if not next: break

            if depth % 2 == 0:
                values = [x.val for x in next]
                values = values[::-1]
                for x, v in zip(next, values):
                    x.val = v
            before = next
            depth += 1

        return root


if __name__ == '__main__':
    pass
