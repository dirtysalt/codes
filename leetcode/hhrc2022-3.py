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
    def lightDistribution(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        repo = set()
        ans = {}

        def walk(root):
            if root is None:
                return ''
            a = walk(root.left)
            b = walk(root.right)
            h = '%s,%s,%s' % (root.val, a, b)
            if h not in repo:
                repo.add(h)
            elif h not in ans:
                ans[h] = root
            return h

        walk(root)
        return list(ans.values())


if __name__ == '__main__':
    pass
