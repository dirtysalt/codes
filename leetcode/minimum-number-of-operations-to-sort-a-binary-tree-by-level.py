#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def dosort(xs):
            from sortedcontainers import SortedList
            sl = SortedList()
            for i in range(len(xs)):
                sl.add((xs[i], i))

            swap = 0
            for i in range(len(xs)):
                value, j = sl.pop(0)
                if value < xs[i]:
                    sl.remove((xs[i], i))
                    sl.add((xs[i], j))
                    xs[j] = xs[i]
                    swap += 1

            # print(xs, swap)
            return swap

        def walk(xs):
            ans = 0
            while xs:
                ans += dosort([x.val for x in xs])
                ss = []
                for x in xs:
                    if x.left:
                        ss.append(x.left)
                    if x.right:
                        ss.append(x.right)
                xs = ss
            return ans

        ans = walk([root])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (aatest_helper.list_to_tree([1, 4, 3, 7, 6, 8, 5, null, null, null, null, 9, null, 10]), 3),
    (aatest_helper.list_to_tree([49, 45, 1, 20, 46, 15, 39, 27, null, null, null, 25]), 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumOperations, cases)

if __name__ == '__main__':
    pass
