#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxValue(self, root: TreeNode, k: int) -> int:

        def walk(root):
            if root is None:
                return [0] * (k+1)

            l = walk(root.left)
            r = walk(root.right)
            res = [0] * (k+1)

            res[0] = max(l) + max(r)

            for i in range(1, k+1):
                for j in range(i):
                    jj = i - 1 - j
                    if jj >=0 and jj < k:
                        res[i] = max(res[i], root.val + l[j] + r[jj])

            return res

        res = walk(root)
        return max(res)

null = None
import aatest_helper
cases = [
    (aatest_helper.list_to_tree([4,1,3,9,null,null,2]), 2, 16),
    (aatest_helper.list_to_tree([5,2,3,4]), 2, 12),
    (aatest_helper.list_to_tree([8,1,3,9,9,9,null,9,5,6,8]), 2, 52),
]

aatest_helper.run_test_cases(Solution().maxValue, cases)



if __name__ == '__main__':
    pass
