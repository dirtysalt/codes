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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        index = {}

        def prepare(root, p):
            if root is None:
                return 0

            index[root.val] = root
            root.parent = p
            lh = prepare(root.left, root)
            rh = prepare(root.right, root)
            root.lh = lh
            root.rh = rh
            return max(lh, rh) + 1

        prepare(root, None)

        record = {}

        def walk(root, h, d):
            l = root.left
            if l is not None:
                h2 = max(root.rh + d, h)
                record[l.val] = h2
                walk(l, h2, d + 1)
            r = root.right
            if r is not None:
                h2 = max(root.lh + d, h)
                record[r.val] = h2
                walk(r, h2, d + 1)

        walk(root, 0, 0)

        ans = []
        for q in queries:
            r = record[q]
            ans.append(r)
        return ans


import aatest_helper

true, false, null = True, False, None
cases = [
    (aatest_helper.list_to_tree([1, 3, 4, 2, null, 6, 5, null, null, null, null, null, 7]), [4], [2]),
    (aatest_helper.list_to_tree([5, 8, 9, 2, 1, 3, 7, 4, 6]), [3, 2, 4, 8], [3, 2, 3, 2])
]

aatest_helper.run_test_cases(Solution().treeQueries, cases)

if __name__ == '__main__':
    pass
