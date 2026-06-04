#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        if len(trees) == 1: return trees[0]

        # collect leaves.
        leaves = {}

        def collect_leaves(t: TreeNode):
            if t is None: return
            if t.left is None and t.right is None:
                leaves[t.val] = t
                return
            collect_leaves(t.left)
            collect_leaves(t.right)

        for t in trees:
            collect_leaves(t)

        # collect roots and find total root.
        subtrees = {}
        root = None
        for t in trees:
            if t.val not in leaves:
                root = t
            subtrees[t.val] = t

        # check if it's ok root.
        def check(node, minB, maxB, cross):
            if node is None: return True
            if node.val <= minB or node.val >= maxB:
                return False

            if node.left is None and node.right is None:
                if node.val in subtrees:
                    x = subtrees[node.val]
                    node.left = x.left
                    node.right = x.right
                    cross[0] += 1

            if not check(node.left, minB, node.val, cross):
                return False
            if not check(node.right, node.val, maxB, cross):
                return False

            return True

        minB, maxB = 0, 1 << 30
        cross = [0]
        if not check(root, minB, maxB, cross):
            return None
        if cross[0] != len(trees) - 1:
            return None

        # import aatest_helper
        # print(aatest_helper.tree_to_list(root))
        return root


true, false, null = True, False, None
import aatest_helper

cases = [
    # ([aatest_helper.list_to_tree(x) for x in [[2, 1], [3, 2, 5], [5, 4]]], aatest_helper.ANYTHING),
    ([aatest_helper.list_to_tree(x) for x in [[5, 3, 8], [3, 2, 6]]], aatest_helper.ANYTHING),
]

aatest_helper.run_test_cases(Solution().canMerge, cases)

if __name__ == '__main__':
    pass
