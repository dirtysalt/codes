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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        from sortedcontainers import SortedList
        sl = SortedList()

        def walk(root):
            if root is None: return
            walk(root.left)
            sl.add(root.val)
            walk(root.right)

        walk(root)
        ans = []
        for q in queries:
            i = sl.bisect_right(q) - 1
            x = sl[i] if i >= 0 and i < len(sl) else -1
            j = sl.bisect_left(q)
            y = sl[j] if j >= 0 and j < len(sl) else -1
            ans.append([x, y])
        return ans


if __name__ == '__main__':
    pass
